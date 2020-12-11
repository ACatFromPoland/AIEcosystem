import time
import random
import math
import pygal
# https://www.geeksforgeeks.org/running-python-script-on-gpu/
# Line chart vars
Rabbit_Count = 0
Rabbit_Population = []

#Generate Array
xGrid = 100
yGrid = 100
GridSize = xGrid * yGrid
'''
def GenerateArray(xGrid, yGrid):
    ouputList = []
    
    for _ in range(xGrid):
        list_ = []
        for _ in range(yGrid):
            list_.append(0)
        ouputList.append(list_)
    return ouputList
'''

'''
        given_xPos = xPos
        given_yPos = yPos
        possibleLocations = [
            (given_xPos - 1,given_yPos - 1),
            (given_xPos,given_yPos - 1),
            (given_xPos + 1,given_yPos - 1),

            (given_xPos - 1,given_yPos),
            (given_xPos + 1,given_yPos),
            (given_xPos - 1,given_yPos - 1),
            (given_xPos - 1,given_yPos - 1),
            (given_xPos - 1,given_yPos - 1),
        ]
        while True:
            if MapArray2D[given_xPos][given_yPos] == 0:
                Entity_Dict.append(Rabbit(given_xPos, given_yPos, givenFood, creatureType, eyeSight, state))
                Rabbit_Count = Rabbit_Count + 1
                return
        '''

MapArray2D = [[0 for i in range(yGrid)] for j in range(xGrid)]

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
    #output += "\n \n \n \n \n"
    print(output)

Entity_Dict = []

class Animal():
    global MapArray2D
    global Rabbit_Count
    global xGrid
    global yGrid
    # Urge to turn
    # Urge to move forward

    def __init__(self, xPos, yPos, foodTotal, creatureType, eyeSight, state):
        self.xPos = xPos
        self.yPos = yPos
        self.foodTotal = foodTotal
        self.creatureType = creatureType
        self.eyeSight = eyeSight
        self.state = state

    def CalculateDistance(self, foodX, foodY, xPos, yPos):
            return math.sqrt((foodX-xPos)**2 + (foodY-yPos)**2)

    def ScanEnviroment(self):
        scanList = []
        LookingFor = 0
        FoundDesire = False
        if self.state == 0 and self.creatureType == 2: #Rabbit look for food
            LookingFor = 1
        elif self.state == 1 and self.creatureType == 2:
            LookingFor = 2
        startX = self.xPos - self.eyeSight
        startY = self.yPos - self.eyeSight
        tempX = startX
        tempY = startY
        scanList.append((tempX, tempY))
        Offset = 1 + (self.eyeSight * 2)
        ScanRange = Offset * Offset
        nextline = 0

        for _ in range(ScanRange -1):
            tempX += 1
            nextline += 1
            if nextline == Offset:
                tempX = startX
                tempY += 1
                nextline = 0
            if tempX == self.xPos and tempY == self.yPos:
                pass
            else:
                scanList.append((tempX, tempY))
            '''
            if tempX >= 0 and tempY >= 0:
                if tempX < xGrid and tempY < yGrid:
                    scanList.append((tempX, tempY))
            '''
            check_index = 0
            for i in scanList:
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
                '''
                if i[0] == self.xPos and i[1] == self.xPos:
                    try:
                        del scanList[check_index]
                        if check_index != 0:
                            check_index -= 1
                    except:
                        pass
                '''
                check_index += 1

        foodList = []
        distanceList = []
        for index in scanList:
            if MapArray2D[index[0]][index[1]] == LookingFor:
                foodList.append(index)
        
        for food in foodList:
            distance = Animal.CalculateDistance(self, food[0], food[1], self.xPos, self.yPos)
            distanceList.append(distance)

        if len(distanceList) > 0:
            closestPoint = distanceList.index(min(distanceList))
            closestPoint = foodList[closestPoint]
            FoundDesire = True
            return FoundDesire, closestPoint
        else:
            FoundDesire = False
            closestPoint = None
            return FoundDesire, closestPoint
        

        
        #if self.state == 1 and self.creatureType == 2: #Rabbit look for mate

    def UpdatePos(self):
        MapArray2D[self.xPos][self.yPos] = self.creatureType
    
    def GetPos(self):
        return self.xPos, self.yPos

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
    
    def GetMate(self, xxpos, yypos):
        global Entity_Dict
        for Entity in Entity_Dict:
            entClass = str(type(Entity))
            if ".Rabbit" in entClass:
                if xxpos == Entity.xPos and yypos == Entity.yPos:
                    Entity.state = 2

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
                    MapArray2D[Ox - 1][Oy + 1] = 2
                    self.xPos -= 1
                    self.yPos += 1
                    if Fy == self.yPos and Fx == self.xPos:
                        self.foodTotal += 5
            except:
                pass

        elif Fy != 9999999 and Fy > Oy and Fx == Ox or randomBool == True and randomInt == 1:
            try:
                # up
                if Animal.CheckIfOutBounds(self, Ox, Oy + 1) == False:
                    MapArray2D[Ox][Oy] = 0
                    MapArray2D[Ox][Oy + 1] = 2
                    self.yPos += 1
                    if Fy == self.yPos and Fx == self.xPos: 
                        self.foodTotal += 5
            except:
                pass

        elif Fy != 9999999 and Fy > Oy and Fx > Ox or randomBool == True and randomInt == 2:
            # up right
            try:
                if Animal.CheckIfOutBounds(self, Ox + 1, Oy + 1) == False:
                    MapArray2D[Ox][Oy] = 0
                    MapArray2D[Ox + 1][Oy + 1] = 2
                    self.xPos += 1
                    self.yPos += 1
                    if Fy == self.yPos and Fx == self.xPos:
                        self.foodTotal += 5
            except:
                pass

        # MIDDLES
        elif Fy != 9999999 and Fy == Oy and Fx < Ox or randomBool == True and randomInt == 3:
            # left
            try:
                if Animal.CheckIfOutBounds(self, Ox - 1, Oy) == False:
                    MapArray2D[Ox][Oy] = 0
                    MapArray2D[Ox - 1][Oy]  = 2
                    self.xPos -= 1
                    if Fy == self.yPos and Fx == self.xPos:
                        self.foodTotal += 5
            except:
                pass
        

        elif Fy != 9999999 and Fy == Oy and Fx > Ox or randomBool == True and randomInt == 4:
            #right
            try:
                if Animal.CheckIfOutBounds(self, Ox + 1, Oy) == False:
                    MapArray2D[Ox][Oy] = 0
                    MapArray2D[Ox + 1][Oy] = 2
                    self.xPos += 1
                    if Fy == self.yPos and Fx == self.xPos:
                        self.foodTotal += 5
            except:
                pass


        # DOWNS
        elif Fy != 9999999 and Fy < Oy and Fx < Ox or randomBool == True and randomInt == 5:
            #down left
            try:
                if Animal.CheckIfOutBounds(self, Ox - 1, Oy - 1) == False:
                    MapArray2D[Ox][Oy] = 0
                    MapArray2D[Ox - 1][Oy - 1] = 2
                    self.xPos -= 1
                    self.yPos -= 1
                    if Fy == self.yPos and Fx == self.xPos:
                        self.foodTotal += 5
            except:
                pass

        elif Fy != 9999999 and Fy < Oy and Fx == Ox or randomBool == True and randomInt == 6:
            #down
            try:
                if Animal.CheckIfOutBounds(self, Ox, Oy - 1) == False:
                    MapArray2D[Ox][Oy] = 0
                    MapArray2D[Ox][Oy - 1] = 2
                    self.yPos -= 1
                    if Fy == self.yPos and Fx == self.xPos:
                        self.foodTotal += 5
            except:
                pass

        elif Fy != 9999999 and Fy < Oy and Fx > Ox or randomBool == True and randomInt == 7:
            #down right
            try:
                if Animal.CheckIfOutBounds(self, Ox + 1, Oy - 1) == False:
                    MapArray2D[Ox][Oy] = 0
                    MapArray2D[Ox + 1][Oy - 1] = 2
                    self.xPos += 1
                    self.yPos -= 1
                    if Fy == self.yPos and Fx == self.xPos:
                        self.foodTotal += 5
            except:
                pass

    def MoveRandomly(self):
        randomint = random.randint(0,7)
        Animal.WalkTo(self, (9999999, 9999999),True, randomint)

    def Update(self):
        global Rabbit_Count
        self.foodTotal -= 1
        
        if self.foodTotal > 60:
            self.state = 1

        elif self.foodTotal < 45:
            self.state = 0

        if self.foodTotal < 0:
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
                #rint(self.xPos, self.yPos)
                #print(MatePos[0], MatePos[1])
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
            

            #if animal is looking for mate  <-- State 1
                #ScanEnviroment
                    #If mate is found
                        # Alert Mate to wait
                        # WalkTo
                    #else
                        #Walk randomly
                    
                    #If mate is close
                        #Have babies

class Rabbit(Animal):
    pass

class Fox(Animal):
    pass

def GenerateRabbit(birth=False, randomSpawn=True, xPos=2, yPos=2, givenFood=0):
    global xGrid
    global yGrid
    global MapArray2D
    global Rabbit_Count
    creatureType = 2
    foodTotal = 50
    eyeSight = 2
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

    elif randomSpawn == False and birth == False: # None Random spawn
        given_xPos = xPos
        given_yPos = yPos
        if MapArray2D[given_xPos][given_yPos] == 0:
            Entity_Dict.append(Rabbit(given_xPos, given_yPos, foodTotal, creatureType, eyeSight, state))
            Rabbit_Count = Rabbit_Count + 1
            return
    
    elif randomSpawn == False and birth == True: # Birth
        while True:
            r_Xpos = random.randint(0, xGrid - 1)
            r_Ypos = random.randint(0, yGrid - 1)
            if MapArray2D[r_Xpos][r_Ypos] == 0:
                Entity_Dict.append(Rabbit(r_Xpos, r_Ypos, givenFood, creatureType, eyeSight, state))
                Rabbit_Count = Rabbit_Count + 1
                break
        return


def GenerateFood():
    global xGrid
    global yGrid
    global MapArray2D

    while True:
        r_Xpos = random.randint(0, xGrid - 1)
        r_Ypos = random.randint(0, yGrid - 1)
        if MapArray2D[r_Xpos][r_Ypos] == 0:
            MapArray2D[r_Xpos][r_Ypos] = 1
            break
    return

def UpdateEcosystem():
    global Entity_Dict
    for Entity in Entity_Dict:
        entClass = str(type(Entity))
        
        if ".Rabbit" in entClass:
            Entity.Update()
    return




def GenerateEcoSystem(Num_of_Food=2, Num_of_Rabbits=1, Num_of_Foxes=0):
    global GridSize
    global Entity_Dict
    for _ in range(Num_of_Food):
        GenerateFood()
    
    for _ in range(Num_of_Rabbits):
        GenerateRabbit(False, True)

    for Entity in Entity_Dict:
        entClass = str(type(Entity))
        
        if ".Rabbit" in entClass:
            Entity.UpdatePos()

    print("Ecosystem Generated")
    return

def GenerateChart():
    line_chart = pygal.Line()
    line_chart.title = 'Rabbit Population'
    line_chart.add('Rabbits', Rabbit_Population)
    line_chart.render_to_file('Line_chart.svg')
    return

in_Food = int(input("Food Count: "))
in_Rabbits = int(input("Rabbit Count: "))
in_Foxes = int(input("Foxes Count: "))

GenerateEcoSystem(in_Food, in_Rabbits, in_Foxes)
UpdateDisplay(MapArray2D, GridSize, xGrid, yGrid)
time.sleep(2)
itteration = 0

while True:
    GenerateFood()
    GenerateFood()
    GenerateFood()

    Rabbit_Population.append(Rabbit_Count)
    UpdateEcosystem()
    
    #UpdateDisplay(MapArray2D, GridSize, xGrid, yGrid)
    #time.sleep(0.2)
    if Rabbit_Count == 0 or itteration > 5000:
        GenerateChart()
        print("Graph Generated")
        break
    itteration += 1