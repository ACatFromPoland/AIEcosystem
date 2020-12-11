import time
import random

from main import yGrid, xGrid

def ScanEnviroment(MapArray2D, Ent_X, Ent_Y, Eyesight=2, LookingFor=1):
    scanList = []
    
    startX = Ent_X - Eyesight
    startY = Ent_Y - Eyesight

    tempX = startX
    tempY = startY

    scanList.append((tempX, tempY))
    numr = 1 + (Eyesight * 2)
    rang = numr * numr

    nextline = 0
    for num in range(rang-1):
        tempX += 1
        nextline += 1
        if nextline == numr:
            tempX = startX
            tempY += 1
            
            nextline = 0
        if tempX > 0 and tempY > 0:
            if tempX < xGrid and tempY < yGrid:
                scanList.append((tempX, tempY))
        

    foundFood = False
    foodx = 0
    foody = 0

    for index in scanList:
        if MapArray2D[index[0]][index[1]] == 1:
            foodx = index[0]
            foody = index[1]
            foundFood = True
            break
        
    
    #print("Scanned")
    return (foodx, foody), foundFood

def Walk(MapArray2D, Ent_X, Ent_Y, Eyesight, LookingFor, AteFood):

    movements = ["up","down","left","right","upleft","upright","downleft","downright"]
    
    if AteFood == True:
        foodXY, FoodFound = ScanEnviroment(MapArray2D, Ent_X, Ent_Y, Eyesight, LookingFor)
        foodX = foodXY[0]
        foodY = foodXY[1]
    if FoodFound == True:
        AteFood = False

        #foodX 4 #rabbitX 3
        #foodY 4 #rabbitY 6
        move = 8

        if foodX == Ent_X and foodY > Ent_Y:
            move = 1# down

        if foodX == Ent_X and foodY < Ent_Y:
            move = 0# up

        if foodX > Ent_X and foodY == Ent_Y:
            move = 3# right

        if foodX < Ent_X and foodY == Ent_Y:
            move = 2# left


        #special
        if foodX < Ent_X and foodY > Ent_Y:
            move = 6# down left

        if foodX > Ent_X and foodY > Ent_Y:
            move = 7# down right

        if foodX < Ent_X and foodY < Ent_Y:
            move = 4# up left

        if foodX > Ent_X and foodY < Ent_Y:
            move = 5# up right

        #special
        #print("move: ", move)
        
    if FoodFound == True:
        #print("Walking", movements[move])
        try:
            return movements[move]
        except:
            print(movements[move])
            print(Crash)
    else:
        #print("Walking somewhere")
        moveSomewhere = random.randint(0,7)
        return movements[moveSomewhere]






#Useless Right now
def Run():
    print("Running")
    return

def Mate():
    print("Mating")
    return
