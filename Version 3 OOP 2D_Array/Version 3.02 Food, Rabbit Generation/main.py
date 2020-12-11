import time
import random

#Generate Array
xGrid = 10
yGrid = 10
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
    output += "\n \n \n \n \n"
    print(output)

Entity_Dict = []

class Animal():
    global MapArray2D

    def __init__(self, xPos, yPos, foodTotal, creatureType):
        self.xPos = xPos
        self.yPos = yPos
        self.foodTotal = foodTotal
        self.creatureType = creatureType

    def UpdatePos(self):
        MapArray2D[self.xPos][self.yPos] = self.creatureType

class Rabbit(Animal):
    pass

def GenerateRabbit(randomSpawn=True, xPos=2, yPos=2):
    global xGrid
    global yGrid
    global MapArray2D
    creatureType = 2
    foodTotal = 30

    if randomSpawn == True:
        while True:
            r_Xpos = random.randint(0, xGrid - 1)
            r_Ypos = random.randint(0, yGrid - 1)
            if MapArray2D[r_Xpos][r_Ypos] == 0:
                Entity_Dict.append(Rabbit(r_Xpos, r_Ypos, foodTotal, creatureType))
                break
        return

    if randomSpawn == False:
        given_xPos = xPos
        given_yPos = yPos
        if MapArray2D[given_xPos][given_yPos] == 0:
            Entity_Dict.append(Rabbit(given_xPos, given_yPos, foodTotal, creatureType))
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
    return

def GenerateEcoSystem(Num_of_Food=5, Num_of_Rabbits=2, Num_of_Foxes=0):
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


GenerateEcoSystem()
UpdateDisplay(MapArray2D, GridSize, xGrid)
time.sleep(5)
while True:
    UpdateEcosystem()
    
    UpdateDisplay(MapArray2D, GridSize, xGrid)
    time.sleep(2)