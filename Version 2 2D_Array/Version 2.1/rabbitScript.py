import time
import random
import AiController


def Rabbit(Entity, MapArray2D): # , MapArray
    Died = False
    
    rabbitX = Entity["posX"]
    rabbitY = Entity["posY"]

    rabbit_food = Entity["food"]
    rabbit_state = Entity["state"]
    rabbit_eyesight = Entity["eyesight"]

    R_AteFood = Entity["AteFood"]
    R_FoundFood = Entity["FoundFood"]

    def RabbitSate(rabbit_state, MapArray2D): # , MapArray
    
        return{
            '0': lambda: AiController.Walk(MapArray2D, rabbitX, rabbitY, rabbit_eyesight, 1, R_AteFood),
            '1': lambda: AiController.Run(),
            '2': lambda: AiController.Mate()
            }.get(rabbit_state, lambda: None)()

    moveTo = RabbitSate(str(rabbit_state), MapArray2D) # , MapArray
    #print("RabbitState", moveTo)
    
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
    #print("Rabbit Food: ", Entity["food"])
    if Entity["food"] <= -1:
        Died = True
    
    return Entity, Died, Moved
