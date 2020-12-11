import time
import random

#from main import yGrid, xGrid

def ScanEnviroment(MapArray2D, xGrid, yGrid, Ent_X, Ent_Y, Eyesight=2, LookingFor=1):
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
        #print("-----",tempX, tempY)
        tempX += 1
        nextline += 1
        if nextline == numr:
            tempX = startX
            tempY += 1
            
            nextline = 0
        if tempX >= 0 and tempY >= 0:
            if tempX <= xGrid or tempY <= yGrid:
                #print(tempX, tempY)
                scanList.append((tempX, tempY))
        
    foundFood = False
    foodx = 0
    foody = 0
    #print(scanList)

    for index in scanList:
        if MapArray2D[index[0]][index[1]] == 1:
            foodx = index[0]
            foody = index[1]
            foundFood = True
            break
        
    
    #print("Scanned;", "Food: ",foundFood)
    return (foodx, foody), foundFood

def Walk(MapArray2D, xGrid, yGrid, Ent_X, Ent_Y, Eyesight, LookingFor, AteFood, FoodFound):
    #print("WALK______")
    #print("FoodFound_1: ", FoodFound)

    movements = ["up","down","left","right","upleft","upright","downleft","downright", "nowhere"]

    #print("Ate food", AteFood)
    if AteFood == True:
        #print("Scanned")
        foodXY, FoodFound = ScanEnviroment(MapArray2D, Ent_X, Ent_Y, Eyesight, LookingFor)
        foodX = foodXY[0]
        foodY = foodXY[1]
    #print("FoodFound_2: ", FoodFound)
    if FoodFound == True:
        AteFood = False

        #foodX 4 #rabbitX 3
        #foodY 4 #rabbitY 6
        move = 8

        if foodX == Ent_X and foodY > Ent_Y:
            #print("AI_down")
            move = 1# down

        if foodX == Ent_X and foodY < Ent_Y:
            #print("AI_up")
            move = 0# up

        if foodX > Ent_X and foodY == Ent_Y:
            #print("AI_right")
            move = 3# right

        if foodX < Ent_X and foodY == Ent_Y:
            #print("AI_left")
            move = 2# left


        #special
        if foodX < Ent_X and foodY > Ent_Y:
            #print("AI_down left")
            move = 6# down left

        if foodX > Ent_X and foodY > Ent_Y:
            #print("AI_down right")
            move = 7# down right

        if foodX < Ent_X and foodY < Ent_Y:
            #print("AI_up left")
            move = 4# up left

        if foodX > Ent_X and foodY < Ent_Y:
            #print("AI_up right")
            move = 5# up right

        #special
        #print("move: ", move)
        
    if FoodFound == True:
        #print(move)
        return movements[move]
    
    elif FoodFound == False:
        moveSomewhere = random.randint(0,7)
        #print("Random", movements[moveSomewhere])
        return movements[moveSomewhere]



#Useless Right now
def Run():
    print("Running")
    return

def Mate():
    print("Mating")
    return
