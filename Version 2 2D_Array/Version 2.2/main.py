import time
import random
import pygal
#Scripts
import rabbitScript
import foxScript

def GenerateHash():
    hash = random.getrandbits(128)
    return hash

# Generate Array
xGrid = 50
yGrid = 50
GridSize = xGrid * yGrid
def GenerateArray(xGrid, yGrid):
    outputList = []
    
    for num in range(xGrid):
        list_ = []
        for x in range(yGrid):
            list_.append(0)
        outputList.append(list_)
    return outputList
if __name__ == '__main__':
    MapArray2D = GenerateArray(xGrid, yGrid)
# Generate Array

##############################################                         Display
def UpdateDisplay(MapArray, Grid, Offset):
    x = 0
    y = 0
    output = ""

    objects = ["` ","@ ","R ","F ","# "]
    
    for i in range(Grid):
        point = MapArray[x][y]
        output += objects[point]
        if x == (Offset - 1):
            x = 0
            y += 1
            output += "\n"
        else:
            x += 1
    return output

def UpdatePos(x, y):
    global MapArray2D
    MapArray2D[x][y] = 2

    return

################################################
EntityDict = []
Rabbit_Count = 0
Total_Rabbit_Count = 0

def GenerateRabbit():     # Generate Rabbit
    global EntityDict
    global MapArray2D
    global Rabbit_Count
    global Total_Rabbit_Count
    global xGrid
    global yGrid
    RandomHash = GenerateHash()
    quickcount = 0

    while True:
        if quickcount > 100:
            break
        quickcount += 1
        randomX = random.randint(0, xGrid -1)
        randomY = random.randint(0, yGrid -1)
        if MapArray2D[randomX][randomY] == 0:
            Rabbit_Count += 1
            Total_Rabbit_Count += 1
            
            name_ = "rabbit"
            state_ = 0
            food_ = 50
            eyesight_ = 2
            AteFood_ = True
            FoundFood_ = False
            
            rabbit = {"creature_ID": RandomHash, "creature": name_ ,"posX": randomX, "posY": randomY ,"state": state_, "food": food_, "eyesight" : eyesight_, "AteFood": AteFood_, "FoundFood": FoundFood_}
            UpdatePos(randomX, randomY)
            break
    
    EntityDict.append(dict(rabbit))
    return

############################################### 
def GenerateFood(posX=0, posY=0, ifbool=False):
    global MapArray2D
    quickcount = 0
    
    while True:
        if quickcount > 100:
            break
        quickcount += 1
        if ifbool == False:
            randomX = random.randint(0, xGrid -1)
            randomY = random.randint(0, yGrid -1)
        else:
            randomX = posX
            randomY = posY
        if MapArray2D[randomX][randomY] == 0:
            MapArray2D[randomX][randomY] = 1
            break


def UpdateEco():#                                       Update Eco
    global EntityDict
    global Rabbit_Count
    global MapArray2D
    
    EntList = EntityDict
    for Entity in EntList:
        if Entity["creature"] == "rabbit":
            #                                        Rabbit                                                   #
            old_X = Entity["posX"]
            old_Y = Entity["posY"]
            
            
            UpdatedEntity, Did_Die, Moved, GenRab = rabbitScript.Rabbit(Entity, MapArray2D, xGrid, yGrid)
            if GenRab == True:
                preg = random.randint(0, 15)
                for x in range(preg):
                    GenerateRabbit()
            
            if Moved == True:
                MapArray2D[old_X][old_Y] = 0

            if Did_Die == False:
                Entity = UpdatedEntity
                UpdatePos(Entity["posX"], Entity["posY"])

            else:
                
                MapArray2D[old_X][old_Y] = 1
                #GenerateFood()
                critterID = Entity["creature_ID"]
                index_del = 0
                for ent in EntityDict:
                    if ent["creature_ID"] == critterID:
                        del EntityDict[index_del]
                        Rabbit_Count -= 1
                        break
                    else:
                        index_del += 1

        elif Entity["creature"] == "fox":
            pass
        
    #for x in range(round(Rabbit_Count / 1)):
    #    GenerateFood()
    
            
######
# PY GAL PY GAL PY GAL PY GAL
timeSteps = 5000
step = 0

rabbitPopulation = []
totalRabbitPop = []

def GenerateGraph():
    global rabbitPopulation
    global totalRabbitPop
    line_chart = pygal.Line()
    line_chart.title = 'Rabbit Population over time'
    
    line_chart.add('Rabbits', rabbitPopulation)
    line_chart.add('Total_Rabbits', totalRabbitPop)
    
    line_chart.render_to_file('Line_chart.svg')

######################################### UPDATE    Update    UPDATE
StartFood = 50
startRabbit = 10
if __name__ == '__main__':
    #Do things
    for x in range(startRabbit):
        GenerateRabbit()

    for x in range(StartFood):
        GenerateFood()
    #GenerateFood()

    while True:
        #GenerateFood()
        step += 1
        rabbitPopulation.append(Rabbit_Count)
        totalRabbitPop.append(Total_Rabbit_Count)
        if step > timeSteps:
            GenerateGraph()
            break
        if Rabbit_Count == 0:
            GenerateGraph()
            break
            
            
        mapDisplay = UpdateDisplay(MapArray2D, GridSize, xGrid)
        print(mapDisplay)
        try:
            UpdateEco()
        except:
            print("Error")
            print(mapDisplay)
            line_chart = pygal.Line()
            line_chart.title = 'Rabbit Population over time'
            line_chart.add('Rabbits', rabbitPopulation)
            line_chart.render_to_file('Line_chart.svg')
            break
        print("Rabbits: ", Rabbit_Count)
        time.sleep(1)
        print("\n\n\n\n\n")
print("Finished")

