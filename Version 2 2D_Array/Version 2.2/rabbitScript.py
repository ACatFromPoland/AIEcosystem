import time
import random
#
import AiController


def Rabbit(Entity, MapArray2D, xGrid, yGrid): # Rabbit
    Died = False
    GenRab = False
    #print("Rabbit()---------")
    rabbitX = Entity["posX"]
    rabbitY = Entity["posY"]
    #print("X:",rabbitX, " Y:",rabbitY)

    rabbit_food = Entity["food"]
    rabbit_state = Entity["state"]
    rabbit_eyesight = Entity["eyesight"]

    R_AteFood = Entity["AteFood"]
    R_FoundFood = Entity["FoundFood"]

    def RabbitSate(rabbit_state, MapArray2D, xGrid, yGrid): # RabbitState
    
        return{
            '0': lambda: AiController.Walk(MapArray2D, xGrid, yGrid, rabbitX, rabbitY, rabbit_eyesight, 1, R_AteFood, R_FoundFood),
            '1': lambda: AiController.Run(),
            '2': lambda: AiController.Mate()
            }.get(rabbit_state, lambda: None)()

    moveTo = RabbitSate(str(rabbit_state), MapArray2D, xGrid, yGrid) # Calling State

    #print("Move to: ",moveTo)
    if moveTo != None:
        Moved = True
        if moveTo == "up":
            Entity["posY"] -= 1
        if moveTo == "down":
            Entity["posY"] += 1
        if moveTo == "left":
            Entity["posX"] -= 1
        if moveTo == "right":
            Entity["posX"] += 1
            
        if moveTo == "upleft":
            Entity["posX"] -= 1
            Entity["posY"] -= 1
        if moveTo == "upright":
            Entity["posX"] += 1
            Entity["posY"] -= 1
        if moveTo == "downleft":
            Entity["posX"] -= 1
            Entity["posY"] += 1
        if moveTo == "downright":
            Entity["posX"] += 1
            Entity["posY"] += 1
    else:
        Moved = False

    Entity["food"] -= 1
    if Entity["food"] <= -1:
        Died = True

    if Entity["posX"] > xGrid or Entity["posX"] < 0:
        Entity["posX"] = rabbitX
    if Entity["posY"] > yGrid or Entity["posY"] < 0:
        Entity["posY"] = rabbitY
    try:
        if MapArray2D[Entity["posX"]][Entity["posY"]] == 1:
            Entity["food"] += 80
            if Entity["food"] > 150:
                Entity["food"] = 100
                GenRab = True
                    
        if MapArray2D[Entity["posX"]][Entity["posY"]] == 2:
                Entity["posX"] = rabbitX
                Entity["posY"] = rabbitY
    except:
        Died = True
            
    return Entity, Died, Moved, GenRab
