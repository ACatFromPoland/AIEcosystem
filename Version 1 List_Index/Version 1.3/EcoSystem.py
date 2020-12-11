import random
import time

import AiTarget
#from AiTarget import *


'''
entlist = [ {"rabbit_1": ('food', 'water')} , {"rabbit_2": ('food', 'water')} ]

new_rabbit = {"rabbit_3": ('food', 'water')}

entlist.append(dict(new_rabbit))
print(entlist)
print(entlist[0]["rabbit_1"][0])

'''


#Update Display
xGrid = 9
yGrid = 9 
mapArray = []
for _ in range(xGrid * yGrid):
    mapArray.append(0)
mapDisplay = ""

def UpdateDisplay(mapAr, cutOf):
    output = ""
    cutOf -= 1
    reset = cutOf

    for point in mapAr:
        if point == 0:
            output += "` "
        elif point == 1:
            output += "@ "
        elif point == 2:
            output += "R "
        elif point == 3:
            output += "F "
        cutOf -= 1
            
        if cutOf == -1:
            output += "\n"
            cutOf = reset

    return output

#EcoSystem


ent_list = []
rabbits = 0
rabbit_name = "rabbit"

def GenerateRabbit():
    global mapArray
    while True:
        ranX = random.randint(0, xGrid - 1)
        ranY = random.randint(0, yGrid - 1)
        random_ = (ranX*1)+(ranY*yGrid)
        if mapArray[random_] == 0:
            return random_

random_start = GenerateRabbit()

starting_rabbit = {"position": random_start,"index": 0, "food": 60, "water": 50, "speed": 1, "want_sex": 0, "state": 0, "gender": "male", "eyesight" : 2}
rabbits += 1
ent_list.append(dict(starting_rabbit))


def GenerateFood():
    global mapArray

    while True:
        ranX = random.randint(0, xGrid - 1)
        ranY = random.randint(0, yGrid - 1)
        random_ = (ranX*1)+(ranY*yGrid)
        if mapArray[random_] == 0:
            mapArray[random_] = 1
            break

def Die(pos_of_death, i):
    global MapArray
    del ent_list[i]
    mapArray[pos_of_death] = 1


# Lists for idiots
# The way the stupid me made this, doesn't allow easy denial of stopping animals from jumping to the other side of a map.
# So this has to be done.


def Rabbit(rabbit):
    global mapArray
    global xGrid
    
    rabbit_pos = rabbit["position"]
    rabbit_food = rabbit["food"]
    rabbit_index = rabbit["index"]
    rabbit_state = rabbit["state"]
    rabbit_eyesight = rabbit["eyesight"]

    eaten = False
    pos = rabbit_pos

    #movementinfo = ["up", "down", "left", "right", "upleft", "upright", "downleft", "downright"]
    
    movementinfo = [pos - xGrid, pos + xGrid, pos -1, pos +1, pos - xGrid - 1, pos + xGrid - 1,  pos - xGrid - 1, pos + xGrid + 1, pos] 

    # States
    # 0 = nothing
    # 1 = food
    # 2 = looking for mate
    # 3 = 

    if rabbit_food < 100:
        rabbit_state = 1
        #rabbit["position"] = rabbit_pos - 1

    if rabbit_state == 0: # Wondering
        #Idle function
        pass

    if rabbit_state == 1: # Looking for food
        move, moved = AiTarget.LookForFood(mapArray, rabbit_pos, xGrid, rabbit_eyesight, 1)
        if moved == True:
            try:
                if movementinfo[move] > (xGrid * xGrid - 1):
                    return
                if movementinfo[move] < 0:
                    return
                #print(mapArray[movementinfo[move]])
                if mapArray[movementinfo[move]] == 0 or mapArray[movementinfo[move]] == 1:
                    if mapArray[movementinfo[move]] == 1:
                        eaten = True
                    mapArray[rabbit_pos] = 0
                    rabbit["position"] = movementinfo[move]
                    moved = False
            except:
                print("ERROR :", "movementinfo > ", movementinfo, "move > ", move)
                print(movementinfo[move])
                return Error
        pass

    if rabbit_state == 2: # Looking to mate
        #Look for mate function
        pass
    
    if eaten == True:
        rabbit_food += 100
        eaten = False
        pass
        
    
    mapArray[rabbit["position"]] = 2
    rabbit_food -= 1
    rabbit["food"] = rabbit_food
    print("rabbits food:", rabbit_food)
    if rabbit_food == 0:
        Die(rabbit_pos, rabbit_index)

    
    return


def Fox():

    return


def UpdateEco(entDict):
    entity_list = entDict
    #print(entity_list)
    
    for entity in entity_list:
        Rabbit(entity)

    return



#Update
#for x in range(1):
    #GenerateFood()
    
while True:
    UpdateEco(ent_list)
    GenerateFood()
    
    mapDisplay = UpdateDisplay(mapArray, xGrid)
    print(mapDisplay)
    time.sleep(0.5)

