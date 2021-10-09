#**************************************************************************************#
#    A simulation of a Fox and Rabbit filled Ecosystem                                 #
#    School project by- Adrian Kazimierski                                             #
#    Date: 2019-2020~                                                                  #
#                                                                                      #
#    Github - https://github.com/ACatFromPoland/AIEcosystem                            #
#    Should be able to run on any python compiler                                      #
#                                                                                      #
#    The entire project runs and prints out everything in the console.                 #
#                                                                                      #
#**************************************************************************************#

import time
import random
import math
import os

import pygal
from tkinter import *
import tkinter as tk

# https://www.geeksforgeeks.org/running-python-script-on-gpu/
# Line chart vars
Rabbit_Popu = 0
RabPopu_year = []
Fox_Popu = 0
FoxPopu_year = []

# Input the amount of Food, Rabbits and foxes that spawn at the start.
in_Food = 0
in_Rabbits = 0
in_Foxes = 0

#Generate Array
ScreenWidthX = 0
ScreenHeightY = 0
ScreenArea = ScreenWidthX * ScreenHeightY

Map2DArray = [[0 for i in range(ScreenHeightY)] for j in range(ScreenWidthX)]

# Simple Display Function
# This takes in the Array of the map, the grid size, the x offset(aka screen width) and the screen height.
# It goes through every square of the grid and makes an output based on each cells state.
# This is only visual and has no control of the program, it can be completely removed.

# In goes
'''[[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]'''
def UpdateDisplay(Map2DArray, Grid, Offset, ScreenHeightY):
    x = 0
    y = ScreenHeightY - 1
    output = ""
    objects = ["` ", "@ ", "R ", "F ", "# "]

    for _ in range(Grid):
        point = Map2DArray[x][y]
        output += objects[point]
        if x == (Offset - 1):
            x = 0
            y -= 1
            output += "\n"
        else:
            x += 1

    print(output)
# Out goes
''' 
` ` ` @
` ` ` `
` ` ` `
` ` ` ` 
'''
   
# This also does the same thing, but results in the output being flipped.
# It also breaks the program so I just decided not to use it.
'''
output = ""
objects = ["` ", "@ ", "R ", "F ", "# "]

for i in Map2DArray:
    for j in i:
        output += objects[j]
    output += "\n"

return output
'''
    
    
Entity_Dict = []

# Animal Class, this is the main class that defines animals.
# This is the object orientated part of my 
class Animal():
    global Map2DArray
    global Rabbit_Popu
    global ScreenWidthX
    global ScreenHeightY
    # Add:>>
    # Urge to turn
    # Urge to move forward

    # Get all Vars
    def __init__(self, xPos, yPos, Total_Food, creatureType, EyeSight_Range, Entity_State):
        self.xPos = xPos
        self.yPos = yPos
        self.Total_Food = Total_Food
        self.creatureType = creatureType
        self.EyeSight_Range = EyeSight_Range
        self.Entity_State = Entity_State

    # Calculates distance between two points
    def CalculateDistance(self, x2, y2, x1, y1):
            return math.sqrt((x2-x1)**2 + (y2-y1)**2)

    #  Function that scans the squares around the animal by the radius of its 'EyeSight_Range'
    def ScanEnviroment(self):
        scanList = []
        LookingFor = 0
        FoundDesire = False
        
        # Since both rabbits and foxes inherit, this is made to identify what the creature is and what its looking for.
        if self.Entity_State == 0 and self.creatureType == 2: #Rabbit looking for food
            LookingFor = 1
        elif self.Entity_State == 1 and self.creatureType == 2: #Rabbit looking for mate
            LookingFor = 2
            
        elif self.Entity_State == 0 and self.creatureType == 3: #Fox looking for food
            LookingFor = 2
        elif self.Entity_State == 1 and self.creatureType == 3: #Fod looking for mate
            LookingFor = 3


        # Setting up variables
        startX = self.xPos - self.EyeSight_Range 
        startY = self.yPos - self.EyeSight_Range 
        tempX = startX
        tempY = startY
        scanList.append((tempX, tempY))
        Offset = 1 + (self.EyeSight_Range * 2)
        ScanRange = Offset * Offset
        nextline = 0

        # Start the scan
        # Check each square around the creature
        for _ in range(ScanRange -1):
            tempX += 1
            nextline += 1
            if nextline == Offset:
                tempX = startX
                tempY += 1
                nextline = 0
            if tempX == self.xPos and tempY == self.yPos:
                pass
            else:
                scanList.append((tempX, tempY)) # Add the nearby grid to the scanList
            
            
            # Check if the searched cell is out of bounds#
            # If it is, remove it.
            # Could probably be done better but I ain't bothered.
            check_index = 0
            for i in scanList:
                if i[0] < 0:
                    try:
                        del scanList[check_index]
                        if check_index != 0:
                            check_index -= 1
                    except:
                        pass
                if i[0] >= ScreenWidthX:
                    try:
                        del scanList[check_index]
                        if check_index != 0:
                            check_index -= 1
                    except:
                        pass
                if i[1] < 0:    
                    try:
                        del scanList[check_index]
                        if check_index != 0:
                            check_index -= 1
                    except:
                        pass
                if i[1] >= ScreenHeightY:
                    try:
                        del scanList[check_index]
                        if check_index != 0:
                            check_index -= 1
                    except:
                        pass
                check_index += 1
        foodList = []
        distanceList = []
        
        # For each pos in the scanList
        # If the index is what the creature is looking for.
        # Add it to the foodList
        for index in scanList:
            if Map2DArray[index[0]][index[1]] == LookingFor:
                foodList.append(index) #Not a good variable name. Its just possible locations.
        
        # Calculate the distance for each point to the creature.
        for food in foodList:
            distance = Animal.CalculateDistance(self, food[0], food[1], self.xPos, self.yPos)
            distanceList.append(distance)

        # using min get the nearest desired object and alert of its position.
        if len(distanceList) > 0: 
            closestPoint = distanceList.index(min(distanceList)) # Choose which way to go by the minimum pos in the list.
            closestPoint = foodList[closestPoint]
            FoundDesire = True
            return FoundDesire, closestPoint
        else:
            FoundDesire = False
            closestPoint = None
            return FoundDesire, closestPoint
        

    # Plots the creatures position on the Grid when called. (Mainly for testing) (Sometimes for debugging)
    def UpdatePos(self):
        Map2DArray[self.xPos][self.yPos] = self.creatureType
    
    # Returns the Position of the creature
    def GetPos(self):
        return self.xPos, self.yPos

    def CheckIfOutBounds(self, xx, yy):
        IsOut = False
        if xx < 0:
            IsOut = True
        elif yy < 0:
            IsOut = True
        elif xx >= ScreenWidthX:
            IsOut = True
        elif yy >= ScreenHeightY:
            IsOut = True
        else:
            IsOut = False
        return IsOut
    
    # Function to find mate and move towards them
    # Signals the mate to wait
    #
    # : Possible Bug
    #   If the mate is moving towards an immobilised mate and dies in the process. The immobilised mate will stay there until it dies
    def GetMate(self, xxpos, yypos):
        global Entity_Dict
        for Entity in Entity_Dict:
            entClass = str(type(Entity))
            if self.creatureType == 2:
                if ".Rabbit" in entClass:
                    if xxpos == Entity.xPos and yypos == Entity.yPos:
                        Entity.Entity_State = 2

            elif self.creatureType == 3:
                if ".Fox" in entClass:
                    if xxpos == Entity.xPos and yypos == Entity.yPos:
                        Entity.Entity_State = 2

    # Walk to function
    # This function is quite problematic as we have a if statement to check which way to move the creature.
    
    def MoveUpon(self, given_X, given_Y, dir_X, dir_Y):
        global Map2DArray
        if Animal.CheckIfOutBounds(self, given_X + dir_X, given_Y + dir_Y) == False:
            Map2DArray[given_X][given_Y] = 0
            Map2DArray[given_X + dir_X][given_Y + dir_Y] = self.creatureType
            self.xPos += dir_X
            self.yPos += dir_Y
    
    def WalkTo(self, WalkToPos, randomBool=False, randomInt=0):
        global Map2DArray
        Fx = WalkToPos[0]
        Fy = WalkToPos[1]
        Ox = self.xPos
        Oy = self.yPos

        # Too lazy and getting close to deadline so this is good enough for finding out which way the animal moves.
        # Think of "9999999" as NULL
        try:
            # Ups
            if Fy != 9999999 and Fy > Oy and Fx < Ox or randomBool == True and randomInt == 0:
                Animal.MoveUpon(self, Ox, Oy, -1, 1)
  
            elif Fy != 9999999 and  Fy > Oy and Fx == Ox or randomBool == True and randomInt == 1:
                Animal.MoveUpon(self, Ox, Oy, 0, 1)

            elif Fy != 9999999 and  Fy > Oy and Fx > Ox or randomBool == True and randomInt == 2:
                Animal.MoveUpon(self, Ox, Oy, 1, 1)
                
            # Middles
            elif Fy != 9999999 and  Fy == Oy and Fx < Ox or randomBool == True and randomInt == 3:
                Animal.MoveUpon(self, Ox, Oy, -1, 0)

            elif Fy != 9999999 and  Fy == Oy and Fx > Ox or randomBool == True and randomInt == 4:
                Animal.MoveUpon(self, Ox, Oy, 1, 0)

            # Downs
            elif Fy != 9999999 and  Fy < Oy and Fx < Ox or randomBool == True and randomInt == 5:
                Animal.MoveUpon(self, Ox, Oy, -1, -1)

            elif Fy != 9999999 and  Fy < Oy and Fx == Ox or randomBool == True and randomInt == 6:
                Animal.MoveUpon(self, Ox, Oy, 0, -1)

            elif Fy != 9999999 and  Fy < Oy and Fx > Ox or randomBool == True and randomInt == 7:
                Animal.MoveUpon(self, Ox, Oy, 1, -1)

            # Directly Ontop
            if Fy != 9999999 and  Fy == self.yPos and Fx == self.xPos:
                if self.creatureType == 2:
                    self.Total_Food += 5
                else:
                    Fox.EatRabbit(self)

        except:
            print("Animal can't move!")
            pass

    # Nice and easy move randomly, generates a random number then passes it through the walk function
    def MoveRandomly(self):
        randomint = random.randint(0,7)
        Animal.WalkTo(self, (9999999, 9999999),True, randomint) # The 9999999 is a lazy way of stopping the code from crashing, basically acts like NULL but without the NULL


class Rabbit(Animal):  # RABBIT_CLASS            This class inherits the Animal class.

    # Rabbit update is the main function which controls all the logic of the creature.
    def RabbitUpdate(self):
        global Rabbit_Popu
        self.Total_Food -= 1
        
        # If the food is greater than 60, look for mate
        if self.Total_Food > 60:
            self.Entity_State = 1

        # If the food is less then 45, look for food
        elif self.Total_Food < 45:
            self.Entity_State = 0
        
        # If the food of the animal is less then 0, kill the animal
        if self.Total_Food < 0: 
            randomChance = random.randint(0, 100)
            if randomChance < 30:
                Map2DArray[self.xPos][self.yPos] = 1
            Entity_Dict.remove(self)
            Rabbit_Popu = Rabbit_Popu - 1
            return
            
        # Find food
        if self.Entity_State == 0:
            FoundFood, FoodPos = Animal.ScanEnviroment(self)
            if FoundFood == True:
                Animal.WalkTo(self, FoodPos)
            else:
                Animal.MoveRandomly(self)
        
        # Find mate
        if self.Entity_State == 1:
            FoundMate, MatePos = Animal.ScanEnviroment(self)
            if FoundMate == True:
                Animal.GetMate(self, MatePos[0], MatePos[1])
                if Animal.CalculateDistance(self, MatePos[0], MatePos[1], self.xPos, self.yPos) < 1.5:
                    self.Entity_State = 0
                    foodGiven = 20
                    self.Total_Food = self.Total_Food - foodGiven
                    GenerateAnimal(0, True ,False, self.xPos, self.yPos, foodGiven)
                else:
                    Animal.WalkTo(self, MatePos)
            else:
                Animal.MoveRandomly(self)
        
        # wait/do nothing
        if self.Entity_State == 2:
            pass


# Fox class, inherits from the Animal class
class Fox(Animal):

    # Eating rabbits requires a bit of extra logic to remove the rabbit from the Entity List unlike
    # When the rabbits position is taken, it will loop through every rabbit until a rabbit has the same XY, it will then consume the rabbit.
    def EatRabbit(self):
        global Rabbit_Popu
        global Entity_Dict
        for Entity in Entity_Dict:
            entClass = str(type(Entity))
            if ".Rabbit" in entClass:
                if self.xPos == Entity.xPos and self.yPos == Entity.yPos:
                    Entity.Entity_State = 2
                    Entity_Dict.remove(Entity)
                    Rabbit_Popu -= 1
                    self.Total_Food += 25
        return

    # Same thing as RabbitUpdate just tuned to foxes 
    def FoxUpdate(self):
        global Fox_Popu
        self.Total_Food -= 2
        #print(self.Total_Food)
        if self.Total_Food > 80: # If the food is greater than 60, look for mate
            self.Entity_State = 1

        elif self.Total_Food < 30: # If the food is less then 45, look for food
            self.Entity_State = 0

        if self.Total_Food < 0:  # If the food of the animal is less then 0, kill the animal
            randomChance = random.randint(0, 100)
            if randomChance < 30:
                Map2DArray[self.xPos][self.yPos] = 1 # Chance to grow food on its corpse
            Entity_Dict.remove(self)
            Fox_Popu = Fox_Popu - 1
            return
            
        # Find food
        if self.Entity_State == 0:
            FoundFood, FoodPos = Animal.ScanEnviroment(self)
            if FoundFood == True:
                Animal.WalkTo(self, FoodPos)
            else:
                Animal.MoveRandomly(self)

        # Find mate
        if self.Entity_State == 1:
            FoundMate, MatePos = Animal.ScanEnviroment(self)
            if FoundMate == True:
                Animal.GetMate(self, MatePos[0], MatePos[1])
                if Animal.CalculateDistance(self, MatePos[0], MatePos[1], self.xPos, self.yPos) < 1.5:
                    self.Entity_State = 0
                    foodGiven = 20
                    self.Total_Food = self.Total_Food - foodGiven
                    GenerateAnimal(1, True ,False, self.xPos, self.yPos, foodGiven)
                else:
                    Animal.WalkTo(self, MatePos)
            else:
                Animal.MoveRandomly(self)
        
        # wait / do nothing
        if self.Entity_State == 2:
            pass
        
# I had to clean it up a bit like can you blame me...
def GenerateAnimal(animalType=99, birth=False, randomSpawn=True, given_X=0, given_Y=0, givenFood=0):
    global ScreenWidthX
    global ScreenHeightY
    global Map2DArray
    global Rabbit_Popu
    global Fox_Popu
    Animal_info = [
        [2,50,4,0],
        [3,50,7,0]
    ]
    if animalType == 99:
        print("Error GenerateAnimal : AnimalType not set.")
        return
    creatureType = Animal_info[animalType][0]
    Total_Food = Animal_info[animalType][1]
    EyeSight_Range = Animal_info[animalType][2]
    Entity_State = Animal_info[animalType][3]

    def NaturalBirth(foodGiven):
        global Rabbit_Popu
        global Fox_Popu
        possibleLocations = [
            (given_X - 1 , given_Y - 1),
            (given_X     , given_Y - 1),
            (given_X + 1 , given_Y - 1),
            (given_X - 1 , given_Y),
            (given_X + 1 , given_Y),
            (given_X - 1 , given_Y + 1),
            (given_X     , given_Y + 1),
            (given_X + 1 , given_Y + 1)
        ]
        stop = -1
        def PickRandom():
            randomSpawnLocation = random.randint(0 , len(possibleLocations) - 1)
            return possibleLocations[randomSpawnLocation][0], possibleLocations[randomSpawnLocation][1]

        random_X, random_Y = PickRandom()
        while True:
            if stop > 8:
                return
            try:
                if Map2DArray[random_X][random_Y] == 0:
                    if animalType == 0:
                        Entity_Dict.append(Rabbit(random_X, random_Y, foodGiven, creatureType, EyeSight_Range, Entity_State))
                        Rabbit_Popu = Rabbit_Popu + 1
                        return
                    elif animalType == 1:
                        Entity_Dict.append(Fox(random_X, random_Y, foodGiven, creatureType, EyeSight_Range, Entity_State)) # This line is what creates the instance of the Fox class and adds it to the Entity_Dict.
                        Fox_Popu = Fox_Popu + 1
                        return
                else:
                    random_X, random_Y = PickRandom()
                    stop += 1

            except:
                random_X, random_Y = PickRandom()
                stop += 1

    if randomSpawn == True and birth == False:
        while True:
            random_X = random.randint(0, ScreenWidthX - 1)
            random_Y = random.randint(0, ScreenHeightY - 1)
            if Map2DArray[random_X][random_Y] == 0:
                if animalType == 0:
                    Entity_Dict.append(Rabbit(random_X, random_Y, Total_Food, creatureType, EyeSight_Range, Entity_State))
                    Rabbit_Popu = Rabbit_Popu + 1
                    break
                elif animalType == 1:
                    Entity_Dict.append(Fox(random_X, random_Y, Total_Food, creatureType, EyeSight_Range, Entity_State)) # This line is what creates the instance of the Fox class and adds it to the Entity_Dict.
                    Fox_Popu = Fox_Popu + 1
                    break

    elif randomSpawn == False and birth == False: # None Random spawn (Mainly for tests)
        if Map2DArray[given_X][given_Y] == 0:
            if animalType == 0:
                Entity_Dict.append(Rabbit(given_X, given_Y, Total_Food, creatureType, EyeSight_Range, Entity_State))
                Rabbit_Popu = Rabbit_Popu + 1
                return
            elif animalType == 1:
                Entity_Dict.append(Fox(given_X, given_Y, Total_Food, creatureType, EyeSight_Range, Entity_State))
                Fox_Popu = Fox_Popu + 1
                return
    
    elif randomSpawn == False and birth == True:
        AnimalAmount = random.randint(1, 14)
        for _ in range(AnimalAmount):
            NaturalBirth(givenFood / AnimalAmount)
            
# This is what actually spawns food around the map each turn.
# It is usually a randomly generated location
def GenerateFood():
    global ScreenWidthX
    global ScreenHeightY
    global Map2DArray

    crashStop = 0
    while True:
        crashStop += 1
        if crashStop > 50:
            break
        # Try to spawn food in a random position, if its empty(0) then spawn it there. Else loop through it again and try to place down food.
        r_Xpos = random.randint(0, ScreenWidthX - 1)
        r_Ypos = random.randint(0, ScreenHeightY - 1)
        if Map2DArray[r_Xpos][r_Ypos] == 0:
            Map2DArray[r_Xpos][r_Ypos] = 1
            break
    return


# The UpdateEcosystem function is looped every turn. It handles each creature and calls its Class Update function
def UpdateEcosystem():
    global Entity_Dict
    
    # For each Entity in the entity dictionary. Check what is the name of the dictionary, if its a rabbit call the RabbitUpdate(), elif its a fox call the FoxUpdate()
    for Entity in Entity_Dict:
        entClass = str(type(Entity))
        
        if ".Rabbit" in entClass:
            Entity.RabbitUpdate()
        elif ".Fox" in entClass:
            Entity.FoxUpdate()
    return

# This is called at the start of the simulation to generate the ecosystem with the input variables
def GenerateEcoSystem(Num_of_Food=2, Num_of_Rabbits=1, Num_of_Foxes=0):
    global ScreenArea
    global Entity_Dict
    for _ in range(Num_of_Food):
        GenerateFood()
    
    for _ in range(Num_of_Rabbits):
        GenerateAnimal(0,False,True)
    
    for _ in range(Num_of_Foxes):
        GenerateAnimal(1,False, True)

    for Entity in Entity_Dict:
        Entity.UpdatePos()

    print("Ecosystem Generated")
    return

# Self explanitory
def GenerateChart():
    line_chart = pygal.Line()
    line_chart.title = 'Rabbit Population'
    line_chart.add('Rabbits', RabPopu_year)
    line_chart.add('Fox', FoxPopu_year)
    line_chart.render_to_file('Line_chart.svg')
    return


#    Main update function, this is what basically loops through everything.
#    Originally it was outside of a function but because of the use of tkinter it was put into a function.
#    This resulted in having to put all the global variables inside.
def MainUpdate(): # foodGui, rabbitsGui, foxGui, xWidth, yHeight
    global ScreenWidthX, ScreenHeightY, Map2DArray, ScreenArea
    global in_Food, in_Rabbits, in_Foxes

    global Entity_Dict
    Entity_Dict.clear()

    global Rabbit_Popu, Fox_Popu    
    Rabbit_Popu = 0
    Fox_Popu = 0

    global FoodGenerationRate

    global RabPopu_year
    RabPopu_year.clear()

    global FoxPopu_year
    FoxPopu_year.clear()

    global itteration
    global itterCount

    in_Food = int(var_Food.get())
    in_Rabbits = int(var_Rab.get())
    in_Foxes = int(var_Fox.get())

    #Generate Array
    ScreenWidthX = int(var_X.get())
    ScreenHeightY = int(var_Y.get())

    checkboxVar = checkBox.get()
        
    ScreenArea = ScreenWidthX * ScreenHeightY

    Map2DArray = [[0 for i in range(ScreenHeightY)] for j in range(ScreenWidthX)]


    # Quickly generates the ecosystem and prints out the display
    GenerateEcoSystem(in_Food, in_Rabbits, in_Foxes)
    UpdateDisplay(Map2DArray, ScreenArea, ScreenWidthX, ScreenHeightY)
    time.sleep(2)

    # This variable is only to count how many times it looped through underneath.
    itteration = 0
    itterCount = 0

    
    #*******************************************************************************************# 
    #                                                                                           #
    #   This is the main loop for the simulation.                                               #
    #   This is currently set to run for "50" days                                              #
    #   Set it to what ever number of time you want                                             #
    #                                                                                           #
    #*******************************************************************************************#

    maxIntteration = 50
    
    while True:

        # A tiny bit of logic to keep food spawns somewhat okay.
        FoodGenerationRate = round(math.sqrt(ScreenArea) / 5)
        for _ in range(FoodGenerationRate * int(GrowthMultipler.get())):
            GenerateFood()

        # Appends the rabbit and fox current population to the total population list.
        RabPopu_year.append(Rabbit_Popu)
        FoxPopu_year.append(Fox_Popu)

        # Update Ecosystem and Update the display.
        UpdateEcosystem()
        if checkboxVar == 1:
            UpdateDisplay(Map2DArray, ScreenArea, ScreenWidthX, ScreenHeightY)
            time.sleep(0.4)

        # If there is no more rabbits or the itterations is over 100. Stop the loop and generate the chart.
        if Rabbit_Popu == 0 and Fox_Popu == 0 or itteration >= maxIntteration:
            GenerateChart()
            print("Graph Generated")
            print("XY position of board : ", "(",var_X.get(),",", var_Y.get(),")")
            print("Number of starting Foxes : ", var_Fox.get())
            print("Number of starting Rabbits : ", var_Rab.get())
            print("Number of starting Food : ", var_Food.get())
            print("Food Growth rate multiplyer : ", GrowthMultipler.get())
            os.startfile('Line_chart.svg')
            break
        #Else just add 1 to itteration (Its kinda a way of keeping track of days.)
        itteration += 1
        itterCount += 1
        if itterCount > 25:
            print("Day: " + str(itteration) + "\n" + "Number of rabbits: " + str(Rabbit_Popu) + "\n" + "Number of foxes: " + str(Fox_Popu))
            itterCount = 0


# Tkinter
# Setting up Tkinter
root = tk.Tk()
root.title("Ecosystem Input")
root.resizable(False, False)

canvas = tk.Canvas(root, height=350, width=350, bg="#0C1A15")
canvas.config(highlightbackground="#0E583E")
canvas.pack(side = 'top')

# Declaring variables
var_X = DoubleVar()
var_Y = DoubleVar()
var_Rab = DoubleVar()
var_Food = DoubleVar()
var_Fox = DoubleVar()


#  XSlider
X = tk.Label(root, text='X Width', bg="#0E583E")
X.config(font=('helvetica', 8))
SliderX = Scale(from_=0, to=100, variable = var_X, orient=HORIZONTAL, bg="#0E583E") 
canvas.create_window(87, 75, window=SliderX)
canvas.create_window(87, 42, window=X)

# YSlider
Y = tk.Label(root, text='Y Height', bg="#0E583E")
Y.config(font=('helvetica', 8))
SliderY = Scale(from_=0, to=100, variable = var_Y, orient=HORIZONTAL, bg="#0E583E")
canvas.create_window(87, 150, window=SliderY)
canvas.create_window(87, 117, window=Y)

# Food Count
Food_Tk = tk.Label(root, text='Food Amount', bg="#0E583E")
Food_Tk.config(font=('helvetica', 8))
Food_Tk_Slider = Scale(from_=0, to=1000, variable = var_Food, orient=HORIZONTAL, bg="#0E583E")
canvas.create_window(262.5, 75-15, window=Food_Tk_Slider)
canvas.create_window(262.5, 42-15, window=Food_Tk)

# Rabbit Count
Rabbit_Tk = tk.Label(root, text='Rabbit Amount', bg="#0E583E")
Rabbit_Tk.config(font=('helvetica', 8))
Rabbit_Tk_Slider = Scale(from_=0, to=1000, variable = var_Rab, orient=HORIZONTAL, bg="#0E583E")
canvas.create_window(262.5, 150-15, window=Rabbit_Tk_Slider)
canvas.create_window(262.5, 117-15, window=Rabbit_Tk)

# Foxes Count
Fox_Tk = tk.Label(root, text='Fox Amount', bg="#0E583E")
Fox_Tk.config(font=('helvetica', 8))
Fox_Tk_Slider = Scale(from_=0, to=1000, variable = var_Fox, orient=HORIZONTAL, bg="#0E583E")
canvas.create_window(262.5, 225-15, window=Fox_Tk_Slider)
canvas.create_window(262.5, 192-15, window=Fox_Tk)

#Growth Rate

GrowthMultipler = DoubleVar()
Growth_Tk = tk.Label(root, text='Food Growth Rate', bg="#0E583E")
Growth_Tk.config(font=('helvetica', 8))
Growth_Slider = Scale(from_=1, to=10, variable = GrowthMultipler, orient=HORIZONTAL, bg="#0E583E")
canvas.create_window(262.5, 300-15, window=Growth_Slider)
canvas.create_window(262.5, 267-15, window=Growth_Tk)


# Check Box
checkBox = IntVar()

Check_Box = tk.Checkbutton(canvas, text="Print Simulation?", padx=10, pady=5, bg="#0E583E", variable=checkBox)
canvas.create_window(87, 225, window=Check_Box)

runSimulator = tk.Button(canvas, text="Run Simulation", padx=2, pady=4, bg="#0E583E", command=MainUpdate)
canvas.create_window(175, 335, window=runSimulator)

root.mainloop()
