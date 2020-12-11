import time
import random
import math
# https://www.geeksforgeeks.org/running-python-script-on-gpu/

#Generate Array
xGrid = 12
yGrid = 12
GridSize = xGrid * yGrid
def GenerateArray(xGrid, yGrid):
    ouputList = []
    
    for _ in range(xGrid):
        list_ = []
        for _ in range(yGrid):
            list_.append(0)
        ouputList.append(list_)
    return ouputList
MapArray2D = GenerateArray(xGrid, yGrid)

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

    def ScanEnviroment(self): #
        scanList = []
        LookingFor = 0
        FoundDesire = False
        if self.state == 0 and self.creatureType == 2: #Rabbit look for food
            LookingFor = 1
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
            scanList.append((tempX, tempY))
            '''
            if tempX >= 0 and tempY >= 0:
                if tempX < xGrid and tempY < yGrid:
                    scanList.append((tempX, tempY))
            '''
            check_index = 0
            for i in scanList:
                #print(i[0], i[1])
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
        for index in scanList:
            #print(LookingFor)
            if MapArray2D[index[0]][index[1]] == LookingFor:
                foodList.append(index)

        def CalculateDistance(self, foodX, foodY, xPos, yPos):
            return math.sqrt((foodX-xPos)**2 + (foodY-yPos)**2)
        
        for food in foodList:
            distance = CalculateDistance(self, food[0], food[1], self.xPos, self.yPos)
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

    def CheckIfOutBounds(self):
        pass

    def WalkTo(self, WalkToPos, randomBool=False, randomInt=0):
        global MapArray2D
        Fx = WalkToPos[0]
        Fy = WalkToPos[1]
        Ox = self.xPos
        Oy = self.yPos

        # UPS
        print(Fy)
        if Fy != 9999999 and Fy > Oy and Fx < Ox or randomBool == True and randomInt == 0:
            try:
                # up left
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
                MapArray2D[Ox][Oy] = 0
                MapArray2D[Ox][Oy + 1] = 2
                self.yPos += 1
                if Fy == self.yPos and Fx == self.xPos: 
                    self.foodTotal += 5
            except:
                pass

        elif Fy != 9999999 and Fy > Oy and Fx < Ox or randomBool == True and randomInt == 2:
            # up right
            print("Moving")
            try:
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
        print(self.foodTotal)
        if self.state == 0:
            FoundFood, FoodPos = Animal.ScanEnviroment(self)
            if FoundFood == True:
                print(FoundFood,": ", FoodPos[0], FoodPos[1])
                Animal.WalkTo(self, FoodPos)
            else:
                print(FoundFood,": ", FoodPos)
                Animal.MoveRandomly(self)

            #if animal is looking for mate  <-- State 1
                #ScanEnviroment
                    #If mate is found
                        # Alert Mate to wait
                        # WalkTo
                    #else
                        #Walk randomly
                    
                    #If mate is close
                        #Have babies



        return

class Rabbit(Animal):
    pass

class Fox(Animal):
    pass

def GenerateRabbit(randomSpawn=True, xPos=2, yPos=2):
    global xGrid
    global yGrid
    global MapArray2D
    creatureType = 2
    foodTotal = 30
    eyeSight = 2
    state = 0

    if randomSpawn == True:
        while True:
            r_Xpos = random.randint(0, xGrid - 1)
            r_Ypos = random.randint(0, yGrid - 1)
            if MapArray2D[r_Xpos][r_Ypos] == 0:
                Entity_Dict.append(Rabbit(r_Xpos, r_Ypos, foodTotal, creatureType, eyeSight, state))
                break
        return

    if randomSpawn == False:
        given_xPos = xPos
        given_yPos = yPos
        if MapArray2D[given_xPos][given_yPos] == 0:
            Entity_Dict.append(Rabbit(given_xPos, given_yPos, foodTotal, creatureType, eyeSight, state))
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
        GenerateRabbit(True)

    for Entity in Entity_Dict:
        entClass = str(type(Entity))
        
        if ".Rabbit" in entClass:
            Entity.UpdatePos()


    print("Ecosystem Generated")
    return

in_Food = int(input("Food Count: "))
in_Rabbits = int(input("Rabbit Count: "))
in_Foxes = int(input("Foxes Count: "))

GenerateEcoSystem(in_Food, in_Rabbits, in_Foxes)
UpdateDisplay(MapArray2D, GridSize, xGrid, yGrid)
time.sleep(2)
while True:
    UpdateEcosystem()
    
    UpdateDisplay(MapArray2D, GridSize, xGrid, yGrid)
    time.sleep(1)