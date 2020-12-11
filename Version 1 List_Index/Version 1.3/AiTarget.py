import time
import random


def ScanEnviroment(mapGrid, position, offset, eyesight=2, state=0):
    mapArray = mapGrid
    scanList = []
    startPos = position - (offset * eyesight) - eyesight
    scanList.append(startPos)

    tempPos = startPos
    tempOffset = offset 
    numr = 1 + (eyesight * 2)
    nextline = 0
    rang = numr * numr

    for num in range(rang - 1):
        tempPos += 1
        nextline += 1
        if nextline == numr:
            tempPos += offset - numr
            nextline = 0
        scanList.append(tempPos)

    foodFound = False
    foodIndex = 0
    
    for index in scanList:
        if index < 0:
            continue
        if index > (offset * offset - 1):
            continue
        try:
            value = mapArray[index]
        except:
            print("Error", index, "At AiTarget: Function Scan Enciroment: value = mapArray[index]")
            return
        if value == state:
            foodFound = True
            foodIndex = index
            break


    return foodFound, foodIndex

def LookForFood(e_mapArray, e_position, e_mapOffset, e_eyesight, e_state):
    #State is what its looking for
    '''
    00 01 02 03 04
    05 06 07 08 09
    10 11 12 13 14
    15 16 17 18 19
    20 21 22 23 24
    '''
    FoundFood, FoodIndex = ScanEnviroment(e_mapArray, e_position, e_mapOffset, e_eyesight, e_state)
    if FoundFood == True:
        #print("Food near")
        #print("Rabbit Pos: ", e_position)
        #print("Food Pos: ", FoodIndex)
        move, moved_s = MoveTo(e_position, FoodIndex)
    else:
        move = Wander()
        #move = 8
        moved_s = True
    
    return move, moved_s

def Wander():
    
    chooseTo = random.randint(0,7)
    return chooseTo

def MoveTo(player, desire):
    pstring = str(player)
    dstring = str(desire)
    if player < 10:
        pstring = "0" + str(player)

    if desire < 10:
        dstring = "0" + str(desire)
    
    pYX = [int(pstring[0]), int(pstring[1])]
    dYX = [int(dstring[0]), int(dstring[1])]


    move = 0
    if dYX[0] == pYX[0] and dYX[1] < pYX[1]: #"left"
        move = 2

    elif dYX[0] == pYX[0] and dYX[1] > pYX[1]: #"right"
        move = 3

    elif dYX[0] > pYX[0] and dYX[1] == pYX[1]: #"down"
        move = 1

    elif dYX[0] < pYX[0] and dYX[1] == pYX[1]: #"up"
        move = 0

    #special 
    elif dYX[0] > pYX[0] and dYX[1] < pYX[1]: #"downleft"
        move = 5

    elif dYX[0] < pYX[0] and dYX[1] < pYX[1]: #"upleft"
        move = 6

    elif dYX[0] > pYX[0] and dYX[1] > pYX[1]: #"downright"
        move = 7

    elif dYX[0] < pYX[0] and dYX[1] > pYX[1]: #"upright"
        move = 4
    #special
    
    return int(move), True
