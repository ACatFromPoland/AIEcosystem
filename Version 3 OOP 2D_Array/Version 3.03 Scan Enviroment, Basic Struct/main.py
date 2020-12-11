import time
import random
import math

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

def UpdateDisplay(MapArray2D, Grid, Offset):
    x = 0
    y = 0
    output = ""
    objects = ["` ", "@ ", "R ", "F ", "# "]

    for _ in range(Grid):
        point = MapArray2D[x][y]
        output += objects[point]
        if x == (Offset - 1):
            x = 0
            y += 1
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
                    del scanList[check_index]
                    check_index -= 1
                if i[0] >= xGrid:
                    del scanList[check_index]
                    check_index -= 1

                if i[1] < 0:    
                    del scanList[check_index]
                    check_index -= 1
                if i[1] >= yGrid:
                    del scanList[check_index]
                    check_index -= 1
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
        # return if it found food and if so where is the closest food

    def UpdatePos(self):
        MapArray2D[self.xPos][self.yPos] = self.creatureType
    
    def Update(self):
        print(Animal.ScanEnviroment(self))
        
        # Get animal state

            #if animal is looking for food <-- State 0
                #ScanEnviroment
                    #If food is found
                        # WalkTo
                    #else 
                        # Walk randomly

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
UpdateDisplay(MapArray2D, GridSize, xGrid)
time.sleep(2)
while True:
    UpdateEcosystem()
    
    UpdateDisplay(MapArray2D, GridSize, xGrid)
    time.sleep(1)