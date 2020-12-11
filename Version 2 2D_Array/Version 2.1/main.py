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
xGrid = 9
yGrid = 9
GridSize = xGrid * yGrid
def GenerateArray(xGrid, yGrid):
    outputList = []
    
    for num in range(xGrid):
        list_ = []
        for x in range(yGrid):
            list_.append(0)
        outputList.append(list_)
    return outputList

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

################################################
EntityDict = []
Rabbit_Count = 0

def GenerateRabbit():     # Generate Rabbit
    global EntityDict
    global MapArray2D
    global Rabbit_Count
    global xGrid
    global yGrid
    RandomHash = GenerateHash()

    while True:
        randomX = random.randint(0, xGrid -1)
        randomY = random.randint(0, yGrid -1)
        if MapArray2D[randomX][randomY] == 0:
            Rabbit_Count += 1
            
            name_ = "rabbit"
            state_ = 0
            food_ = 15
            eyesight_ = 2
            AteFood_ = True
            FoundFood_ = False
            
            rabbit = {"creature_ID": RandomHash, "creature": name_ ,"posX": randomX, "posY": randomY ,"state": state_, "food": food_, "eyesight" : eyesight_, "AteFood": AteFood_, "FoundFood": FoundFood_}
            break
    
    EntityDict.append(dict(rabbit))

GenerateRabbit()
GenerateRabbit()
GenerateRabbit()

############################################### 
def GenerateFood():
    global MapArray2D
    
    while True:
        randomX = random.randint(0, xGrid -1)
        randomY = random.randint(0, yGrid -1)
        if MapArray2D[randomX][randomY] == 0:
            MapArray2D[randomX][randomY] = 1
            break


def UpdateEco():#                                       Update Eco
    global EntityDict
    global Rabbit_Count
    EntList = EntityDict

    for Entity in EntList:
        if Entity["creature"] == "rabbit":
            #                                  Rabbit                                                   #
            old_X = Entity["posX"]
            old_Y = Entity["posY"]
            
            UpdatedEntity, Did_Die, Moved = rabbitScript.Rabbit(Entity, MapArray2D) #
            if Moved == True:
                #print("Deleted")
                try:
                    MapArray2D[old_X][old_Y] = 0
                except:
                    print(old_X, old_Y)
                    print(Crash)

            if Did_Die == False:
                Entity = UpdatedEntity
                try:
                    if MapArray2D[Entity["posX"]][Entity["posY"]] == 1:
                        Entity["food"] += 10
                        if Entity["food"] > 30:
                            Entity["food"] = 10
                            GenerateRabbit()
                except:
                    pass
            else:
                MapArray2D[old_X][old_Y] = 1

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
    for x in range(round(Rabbit_Count / 3)):
        GenerateFood()
            
            
######
# PY GAL PY GAL PY GAL PY GAL
timeSteps = 1000
step = 0
rabbitPopulation = []



######################################### UPDATE    Update    UPDATE
if __name__ == '__main__':
    while True:
        step += 1
        rabbitPopulation.append(Rabbit_Count)
        if step > timeSteps:
            line_chart = pygal.Line()
            line_chart.title = 'Rabbit Population over time'
            line_chart.add('Rabbits', rabbitPopulation)
            line_chart.render_to_file('Line_chart.svg')
            break
        
        UpdateEco()
        #print("Rabbits: ", Rabbit_Count)
        
        mapDisplay = UpdateDisplay(MapArray2D, GridSize, xGrid)
        #print(mapDisplay)
        #time.sleep(1)
