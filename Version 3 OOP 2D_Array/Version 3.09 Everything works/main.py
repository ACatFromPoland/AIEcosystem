import time
import random
import math
import pygal
# https://www.geeksforgeeks.org/running-python-script-on-gpu/
# Line chart vars
Rabbit_Count = 0
Rabbit_Population = []

Fox_Count = 0
Fox_Population = []

#Generate Array
xGrid = int(input("Xgrid: "))
yGrid = int(input("Ygrid: "))
GridSize = xGrid * yGrid

MapArray2D = [[0 for i in range(yGrid)] for j in range(xGrid)]

#   Simple Display Function
def UpdateDisplay(MapArray2D, Grid, Offset, yGrid):
    x = 0
    y = yGrid - 1
    output = ""
    objects = ["` ", "@ ", "R ", "F ", "# "]

    for _ in range(Grid):
        point = MapArray2D[x][y]
        output += objects[point]
        if x == (Offset - 1):
            x = 0
            y -= 1
            output += "\n"
        else:
            x += 1

    print(output)

'''
def UpdateDisplay(MapArray2D, Grid, Offset, yGrid):
    output = ""
    objects = ["` ", "@ ", "R ", "F ", "# "]
    for i in xGrid:
        for j in yGrid:
            output += objects[j]
'''         


Entity_Dict = []

class Animal():
    global MapArray2D
    global Rabbit_Count
    global xGrid
    global yGrid
    # Add:>>
    # Urge to turn
    # Urge to move forward

    # Get all Vars
    def __init__(self, xPos, yPos, foodTotal, creatureType, eyeSight, state):
        self.xPos = xPos
        self.yPos = yPos
        self.foodTotal = foodTotal
        self.creatureType = creatureType
        self.eyeSight = eyeSight
        self.state = state

    # Point distance Calculator
    def CalculateDistance(self, foodX, foodY, xPos, yPos):
            return math.sqrt((foodX-xPos)**2 + (foodY-yPos)**2)


    #                       Function that scans the squares around the animal by the radius of its eyesight
    def ScanEnviroment(self):
        scanList = []
        LookingFor = 0
        FoundDesire = False
        if self.state == 0 and self.creatureType == 2: #Rabbit looking for food
            LookingFor = 1
        elif self.state == 1 and self.creatureType == 2: #Rabbit looking for mate
            LookingFor = 2
            
        elif self.state == 0 and self.creatureType == 3: #Fox looking for food
            LookingFor = 2
        elif self.state == 1 and self.creatureType == 3: #Fod looking for mate
            LookingFor = 3

        startX = self.xPos - self.eyeSight # Setting the start scan pos 
        startY = self.yPos - self.eyeSight #
        tempX = startX
        tempY = startY
        scanList.append((tempX, tempY))
        Offset = 1 + (self.eyeSight * 2)
        ScanRange = Offset * Offset
        nextline = 0

        for _ in range(ScanRange -1): # For the range of the scan, 
            tempX += 1
            nextline += 1
            if nextline == Offset:
                tempX = startX
                tempY += 1
                nextline = 0
            if tempX == self.xPos and tempY == self.yPos:
                pass
            else:
                scanList.append((tempX, tempY)) # Add the nearby grid to the scanList

            check_index = 0
            for i in scanList: # For the scanlist, if its out of bounds. Remove it
                if i[0] < 0:
                    try:
                        del scanList[check_index]
                        if check_index != 0:
                            check_index -= 1
                    except:
                        pass
                if i[0] >= xGrid:
                    try:
                        del scanList[check_index]
                        if check_index != 0:
                            check_index -= 1
                    except:
                        pass
                if i[1] < 0:    
                    try:
                        del scanList[check_index]
                        if check_index != 0:
                            check_index -= 1
                    except:
                        pass
                if i[1] >= yGrid:
                    try:
                        del scanList[check_index]
                        if check_index != 0:
                            check_index -= 1
                    except:
                        pass
                check_index += 1

        foodList = []
        distanceList = []
        for index in scanList: #  For the pos in scanList, if its what the animal is looking for. Add it to foodList
            if MapArray2D[index[0]][index[1]] == LookingFor:
                foodList.append(index) #Not a good variable name. Its just possible locations.
        
        for food in foodList: # Calculate the distance for each point to the creature.
            distance = Animal.CalculateDistance(self, food[0], food[1], self.xPos, self.yPos)
            distanceList.append(distance)

        if len(distanceList) > 0: 
            closestPoint = distanceList.index(min(distanceList)) # Choose which way to go by the minimum pos in the list.
            closestPoint = foodList[closestPoint]
            FoundDesire = True
            return FoundDesire, closestPoint
        else:
            FoundDesire = False
            closestPoint = None
            return FoundDesire, closestPoint
        

    # Plots the creatures position on the Grid when called. (Mainly for testing)
    def UpdatePos(self):
        MapArray2D[self.xPos][self.yPos] = self.creatureType
    
    # Returns the Position of the creature
    def GetPos(self):
        return self.xPos, self.yPos

    # Read the function name
    def CheckIfOutBounds(self, xx, yy):
        IsOut = False
        if xx < 0:
            IsOut = True
        elif yy < 0:
            IsOut = True
        elif xx >= xGrid:
            IsOut = True
        elif yy >= yGrid:
            IsOut = True
        else:
            IsOut = False
        return IsOut
    
    # Function to find mate and move towards them
    def GetMate(self, xxpos, yypos):
        global Entity_Dict
        for Entity in Entity_Dict:
            entClass = str(type(Entity))
            if self.creatureType == 2:
                if ".Rabbit" in entClass:
                    if xxpos == Entity.xPos and yypos == Entity.yPos:
                        Entity.state = 2

            elif self.creatureType == 3:
                if ".Fox" in entClass:
                    if xxpos == Entity.xPos and yypos == Entity.yPos:
                        Entity.state = 2

    # WALK TO FUNCTION                                         <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< THIS is the issue maker.
    def WalkTo(self, WalkToPos, randomBool=False, randomInt=0):
        global MapArray2D
        Fx = WalkToPos[0]
        Fy = WalkToPos[1]
        Ox = self.xPos
        Oy = self.yPos

        # UPS  
        if Fy != 9999999 and Fy > Oy and Fx < Ox or randomBool == True and randomInt == 0:
            try:
                # up left
                if Animal.CheckIfOutBounds(self, Ox - 1, Oy + 1) == False:
                    MapArray2D[Ox][Oy] = 0
                    MapArray2D[Ox - 1][Oy + 1] = self.creatureType
                    self.xPos -= 1
                    self.yPos += 1
                    if Fy == self.yPos and Fx == self.xPos:
                        if self.creatureType == 2:
                            self.foodTotal += 5
                        else:
                            Fox.EatRabbit(self)
            except:
                pass

        elif Fy != 9999999 and Fy > Oy and Fx == Ox or randomBool == True and randomInt == 1:
            try:
                # up
                if Animal.CheckIfOutBounds(self, Ox, Oy + 1) == False:
                    MapArray2D[Ox][Oy] = 0
                    MapArray2D[Ox][Oy + 1] = self.creatureType
                    self.yPos += 1
                    if Fy == self.yPos and Fx == self.xPos: 
                        if self.creatureType == 2:
                            self.foodTotal += 5
                        else:
                            Fox.EatRabbit(self)
            except:
                pass

        elif Fy != 9999999 and Fy > Oy and Fx > Ox or randomBool == True and randomInt == 2:
            # up right
            try:
                if Animal.CheckIfOutBounds(self, Ox + 1, Oy + 1) == False:
                    MapArray2D[Ox][Oy] = 0
                    MapArray2D[Ox + 1][Oy + 1] = self.creatureType
                    self.xPos += 1
                    self.yPos += 1
                    if Fy == self.yPos and Fx == self.xPos:
                        if self.creatureType == 2:
                            self.foodTotal += 5
                        else:
                            Fox.EatRabbit(self)
            except:
                pass

        # MIDDLES
        elif Fy != 9999999 and Fy == Oy and Fx < Ox or randomBool == True and randomInt == 3:
            # left
            try:
                if Animal.CheckIfOutBounds(self, Ox - 1, Oy) == False:
                    MapArray2D[Ox][Oy] = 0
                    MapArray2D[Ox - 1][Oy]  = self.creatureType
                    self.xPos -= 1
                    if Fy == self.yPos and Fx == self.xPos:
                        if self.creatureType == 2:
                            self.foodTotal += 5
                        else:
                            Fox.EatRabbit(self)
            except:
                pass
        

        elif Fy != 9999999 and Fy == Oy and Fx > Ox or randomBool == True and randomInt == 4:
            #right
            try:
                if Animal.CheckIfOutBounds(self, Ox + 1, Oy) == False:
                    MapArray2D[Ox][Oy] = 0
                    MapArray2D[Ox + 1][Oy] = self.creatureType
                    self.xPos += 1
                    if Fy == self.yPos and Fx == self.xPos:
                        if self.creatureType == 2:
                            self.foodTotal += 5
                        else:
                            Fox.EatRabbit(self)
            except:
                pass


        # DOWNS
        elif Fy != 9999999 and Fy < Oy and Fx < Ox or randomBool == True and randomInt == 5:
            #down left
            try:
                if Animal.CheckIfOutBounds(self, Ox - 1, Oy - 1) == False:
                    MapArray2D[Ox][Oy] = 0
                    MapArray2D[Ox - 1][Oy - 1] = self.creatureType
                    self.xPos -= 1
                    self.yPos -= 1
                    if Fy == self.yPos and Fx == self.xPos:
                        if self.creatureType == 2:
                            self.foodTotal += 5
                        else:
                            Fox.EatRabbit(self)
            except:
                pass

        elif Fy != 9999999 and Fy < Oy and Fx == Ox or randomBool == True and randomInt == 6:
            #down
            try:
                if Animal.CheckIfOutBounds(self, Ox, Oy - 1) == False:
                    MapArray2D[Ox][Oy] = 0
                    MapArray2D[Ox][Oy - 1] = self.creatureType
                    self.yPos -= 1
                    if Fy == self.yPos and Fx == self.xPos:
                        if self.creatureType == 2:
                            self.foodTotal += 5
                        else:
                            Fox.EatRabbit(self)
            except:
                pass

        elif Fy != 9999999 and Fy < Oy and Fx > Ox or randomBool == True and randomInt == 7:
            #down right
            try:
                if Animal.CheckIfOutBounds(self, Ox + 1, Oy - 1) == False:
                    MapArray2D[Ox][Oy] = 0
                    MapArray2D[Ox + 1][Oy - 1] = self.creatureType
                    self.xPos += 1
                    self.yPos -= 1
                    if Fy == self.yPos and Fx == self.xPos:
                        if self.creatureType == 2:
                            self.foodTotal += 5
                        else:
                            Fox.EatRabbit(self)
            except:
                pass

    # Nice and easy move randomly,   generates a random number then passes it through the walk function
    def MoveRandomly(self):
        randomint = random.randint(0,7)
        Animal.WalkTo(self, (9999999, 9999999),True, randomint)


class Rabbit(Animal):  # RABBIT_CLASS

    # Rabbit update is the main function which controls all the logic of the creature.
    def RabbitUpdate(self):
        global Rabbit_Count
        self.foodTotal -= 1
        
        if self.foodTotal > 60: # If the food is greater than 60, look for mate
            self.state = 1

        elif self.foodTotal < 45: # If the food is less then 45, look for food
            self.state = 0

        if self.foodTotal < 0:  # If the food of the animal is less then 0, kill the animal
            MapArray2D[self.xPos][self.yPos] = 1
            Entity_Dict.remove(self)
            Rabbit_Count = Rabbit_Count - 1
            return
            
        if self.state == 0: # Find food
            FoundFood, FoodPos = Animal.ScanEnviroment(self)
            if FoundFood == True:
                Animal.WalkTo(self, FoodPos)
            else:
                Animal.MoveRandomly(self)

        if self.state == 1: # Find mate
            FoundMate, MatePos = Animal.ScanEnviroment(self)
            if FoundMate == True:
                Animal.GetMate(self, MatePos[0], MatePos[1])
                if Animal.CalculateDistance(self, MatePos[0], MatePos[1], self.xPos, self.yPos) < 1.5:
                    self.state = 0
                    foodGiven = 20
                    self.foodTotal = self.foodTotal - foodGiven
                    GenerateRabbit(True ,False, self.xPos, self.yPos, foodGiven)
                else:
                    Animal.WalkTo(self, MatePos)
            else:
                Animal.MoveRandomly(self)
        
        if self.state == 2: # wait
            pass

class Fox(Animal):

    def EatRabbit(self):
        global Rabbit_Count
        global Entity_Dict
        for Entity in Entity_Dict:
            entClass = str(type(Entity))
            if ".Rabbit" in entClass:
                if self.xPos == Entity.xPos and self.yPos == Entity.yPos:
                    Entity.state = 2
                    Entity_Dict.remove(Entity)
                    Rabbit_Count -= 1
                    self.foodTotal += 10
        return

    # Same thing as RabbitUpdate just tooned to foxes 
    def FoxUpdate(self):
        global Fox_Count
        self.foodTotal -= 1
        print(self.foodTotal)
        if self.foodTotal > 60: # If the food is greater than 60, look for mate
            self.state = 1

        elif self.foodTotal < 45: # If the food is less then 45, look for food
            self.state = 0

        if self.foodTotal < 0:  # If the food of the animal is less then 0, kill the animal
            MapArray2D[self.xPos][self.yPos] = 1
            Entity_Dict.remove(self)
            Fox_Count = Fox_Count - 1
            return
            
        if self.state == 0: # Find food
            FoundFood, FoodPos = Animal.ScanEnviroment(self)
            if FoundFood == True:
                Animal.WalkTo(self, FoodPos)
            else:
                Animal.MoveRandomly(self)

        if self.state == 1: # Find mate
            FoundMate, MatePos = Animal.ScanEnviroment(self)
            if FoundMate == True:
                Animal.GetMate(self, MatePos[0], MatePos[1])
                if Animal.CalculateDistance(self, MatePos[0], MatePos[1], self.xPos, self.yPos) < 1.5:
                    self.state = 0
                    foodGiven = 20
                    self.foodTotal = self.foodTotal - foodGiven
                    GenerateFox(True ,False, self.xPos, self.yPos, foodGiven)
                else:
                    Animal.WalkTo(self, MatePos)
            else:
                Animal.MoveRandomly(self)
        
        if self.state == 2: # wait
            pass


def GenerateRabbit(birth=False, randomSpawn=True, xPos=0, yPos=0, givenFood=0):
    global xGrid
    global yGrid
    global MapArray2D
    global Rabbit_Count
    creatureType = 2
    foodTotal = 50
    eyeSight = 4
    state = 0

    if randomSpawn == True and birth == False: # Random spawn
        while True:
            r_Xpos = random.randint(0, xGrid - 1)
            r_Ypos = random.randint(0, yGrid - 1)
            if MapArray2D[r_Xpos][r_Ypos] == 0:
                Entity_Dict.append(Rabbit(r_Xpos, r_Ypos, foodTotal, creatureType, eyeSight, state))
                Rabbit_Count = Rabbit_Count + 1
                break
        return

    elif randomSpawn == False and birth == False: # None Random spawn (Mainly for tests)
        given_xPos = xPos
        given_yPos = yPos
        if MapArray2D[given_xPos][given_yPos] == 0:
            Entity_Dict.append(Rabbit(given_xPos, given_yPos, foodTotal, creatureType, eyeSight, state))
            Rabbit_Count = Rabbit_Count + 1
            return

    elif randomSpawn == False and birth == True: # Spawn by birth
        given_xPos = xPos
        given_yPos = yPos
        possibleLocations = [(given_xPos - 1,given_yPos - 1),(given_xPos,given_yPos - 1),(given_xPos + 1,given_yPos - 1),(given_xPos - 1,given_yPos),(given_xPos + 1,given_yPos),(given_xPos - 1,given_yPos + 1),(given_xPos,given_yPos + 1),(given_xPos + 1,given_yPos + 1)]
        randomSpawn = random.randint(0, len(possibleLocations) - 1)
        xxx = possibleLocations[randomSpawn][0]
        yyy = possibleLocations[randomSpawn][1]
        stop = 0
        while True:
            if stop > 8:
                return
            try:
                if MapArray2D[xxx][yyy] == 0:
                    Entity_Dict.append(Rabbit(xxx, yyy, givenFood, creatureType, eyeSight, state)) # This line is what creates the instance of the Rabbit class and adds it to the Entity_Dict.
                    Rabbit_Count = Rabbit_Count + 1
                    return
                else:
                    randomSpawn = random.randint(0, len(possibleLocations) - 1)
                    xxx = possibleLocations[randomSpawn][0]
                    yyy = possibleLocations[randomSpawn][1]
                    stop += 1
            except:
                randomSpawn = random.randint(0, len(possibleLocations) - 1)
                xxx = possibleLocations[randomSpawn][0]
                yyy = possibleLocations[randomSpawn][1]
                stop += 1


def GenerateFox(birth=False, randomSpawn=True, xPos=0, yPos=0, givenFood=0):
    global xGrid
    global yGrid
    global MapArray2D
    global Fox_Count
    creatureType = 3
    foodTotal = 50
    eyeSight = 7
    state = 0

    if randomSpawn == True and birth == False: # Random spawn
        while True:
            r_Xpos = random.randint(0, xGrid - 1)
            r_Ypos = random.randint(0, yGrid - 1)
            if MapArray2D[r_Xpos][r_Ypos] == 0:
                Entity_Dict.append(Fox(r_Xpos, r_Ypos, foodTotal, creatureType, eyeSight, state)) # This line is what creates the instance of the Fox class and adds it to the Entity_Dict.
                Fox_Count = Fox_Count + 1
                break
        return

    elif randomSpawn == False and birth == False: # None Random spawn (MAINLY FOR TESTING)
        given_xPos = xPos
        given_yPos = yPos
        if MapArray2D[given_xPos][given_yPos] == 0:
            Entity_Dict.append(Fox(given_xPos, given_yPos, foodTotal, creatureType, eyeSight, state))
            Fox_Count = Fox_Count + 1
            return

    elif randomSpawn == False and birth == True: # Spawn by birth
        given_xPos = xPos
        given_yPos = yPos
        possibleLocations = [(given_xPos - 1,given_yPos - 1),(given_xPos,given_yPos - 1),(given_xPos + 1,given_yPos - 1),(given_xPos - 1,given_yPos),(given_xPos + 1,given_yPos),(given_xPos - 1,given_yPos + 1),(given_xPos,given_yPos + 1),(given_xPos + 1,given_yPos + 1)]
        randomSpawn = random.randint(0, len(possibleLocations) - 1)
        xxx = possibleLocations[randomSpawn][0]
        yyy = possibleLocations[randomSpawn][1]
        stop = 0
        while True:
            if stop > 8:
                return
            try:
                if MapArray2D[xxx][yyy] == 0:
                    Entity_Dict.append(Fox(xxx, yyy, givenFood, creatureType, eyeSight, state))
                    Fox_Count = Fox_Count + 1
                    return
                else:
                    randomSpawn = random.randint(0, len(possibleLocations) - 1)
                    xxx = possibleLocations[randomSpawn][0]
                    yyy = possibleLocations[randomSpawn][1]
                    stop += 1
            except:
                randomSpawn = random.randint(0, len(possibleLocations) - 1)
                xxx = possibleLocations[randomSpawn][0]
                yyy = possibleLocations[randomSpawn][1]
                stop += 1

def GenerateFood():
    global xGrid
    global yGrid
    global MapArray2D

    while True:
        # Try to spawn food in a random position, if its empty(0) then spawn it there. Else loop through it again and try to place down food.
        r_Xpos = random.randint(0, xGrid - 1)
        r_Ypos = random.randint(0, yGrid - 1)
        if MapArray2D[r_Xpos][r_Ypos] == 0:
            MapArray2D[r_Xpos][r_Ypos] = 1
            break
    return


def UpdateEcosystem():
    global Entity_Dict
    
    # For each Entity in the entity dictionary. Check what is the name of the dictionary, if its a rabbit call the RabbitUpdate(), elif its a fox call the FoxUpdate()
    for Entity in Entity_Dict:
        entClass = str(type(Entity))
        
        if ".Rabbit" in entClass:
            Entity.RabbitUpdate()
        elif ".Fox" in entClass:
            Entity.FoxUpdate()
    return


def GenerateEcoSystem(Num_of_Food=2, Num_of_Rabbits=1, Num_of_Foxes=0):
    global GridSize
    global Entity_Dict
    for _ in range(Num_of_Food):
        GenerateFood()
    
    for _ in range(Num_of_Rabbits):
        GenerateRabbit(False,True)
    
    for _ in range(Num_of_Foxes):
        GenerateFox(False, True)

    for Entity in Entity_Dict:
        Entity.UpdatePos()

    print("Ecosystem Generated")
    return

def GenerateChart():
    line_chart = pygal.Line()
    line_chart.title = 'Rabbit Population'
    line_chart.add('Rabbits', Rabbit_Population)
    line_chart.add('Fox', Fox_Population)
    line_chart.render_to_file('Line_chart.svg')
    return

# Input the amount of Food, Rabbits and foxes that spawn at the start.
in_Food = int(input("Food Count: "))
in_Rabbits = int(input("Rabbit Count: "))
in_Foxes = int(input("Foxes Count: "))

# Quickly generates the ecosystem and prints out the display
GenerateEcoSystem(in_Food, in_Rabbits, in_Foxes)
UpdateDisplay(MapArray2D, GridSize, xGrid, yGrid)
time.sleep(2)

# This variable is only to count how many times it looped through underneath.
itteration = 0
itterCount = 0

FoodGenerationRate = round(Rabbit_Count / 8)


#    Main update function, this is what basically loops through everything.
while True:

    # A tiny bit of logic to keep food spawns somewhat okay.
    if Rabbit_Count < 8:
        FoodGenerationRate = round(GridSize / 100)
        if FoodGenerationRate < 0:
            FoodGenerationRate = 1
    else:
        FoodGenerationRate = round(Rabbit_Count / 8)
    for _ in range(FoodGenerationRate):
        GenerateFood()

    # Appends the rabbit and fox current population to the total population list.
    Rabbit_Population.append(Rabbit_Count)
    Fox_Population.append(Fox_Count)

    # Update Ecosystem and Update the display.
    UpdateEcosystem()
    UpdateDisplay(MapArray2D, GridSize, xGrid, yGrid)
    time.sleep(0.6)

    # If there is no more rabbits or the itterations is over 100. Stop the loop and generate the chart.
    if Rabbit_Count == 0 or itteration > 100:
        GenerateChart()
        print("Graph Generated")
        break
    #Else just add 1 to itteration (Its kinda a way of keeping track of days.)
    itteration += 1
    itterCount += 1
    if itterCount > 30:
        print(Rabbit_Count)
        itterCount = 0