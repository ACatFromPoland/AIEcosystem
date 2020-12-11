import time
import random

#Generate Array
xGrid = 4
yGrid = 4
GridSize = xGrid * yGrid

# We want a 2D Array for our map to store all the states of each box on the grid.
# This function is called only once to Generate the list containing all the states aka the Map Grid
# 
'''
def GenerateArray(xGrid, yGrid):
    ouputList = [] #Set up the output list
    
    for _ in range(xGrid): 
        list_ = []
        for _ in range(yGrid):
            list_.append(0) # I use 0's to represent empty space in my project
        ouputList.append(list_)
    return ouputList
'''
MapArray2D = [[0 for i in range(yGrid)] for j in range(xGrid)]

# The output of this function, if the xGrid and yGrid are 4. Should be ?
'''
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
'''
# This is how the information of the Grid is stored. It doesn't look pretty and it can be hard to read. 
# So if we want to make this look readable and allow us to visualise our project.
# I came up with the idea of dispalying the list with characters.
# We want to convert that list of 0's into something like this.
'''
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
'''
# Then make a **printable** string to output in the console for us to look at
# I use this " ` " to represent empty space in the string
# So our new output should look something like this 
'''
mapstring = (` ` ` ` \n ` ` ` `\n ` ` ` ` \n ` ` ` ` \n)
'''
#When printed out with print(mapstring), it looks something like
''' 
` ` ` `
` ` ` `
` ` ` `
` ` ` ` 
'''

# To get this desired output I use a function called Update_Display()
def UpdateDisplay(MapArray2D, Grid, Offset, yGrid): # It takes in the Grid, Grid Size, the offset of X and starting position of Y
    x = 0 # This determines where we start the scan
    y = yGrid - 1 # We want to start at the top to have the grid display correctly and not upside down. 
    #               ( the number 4 is represented as 0,1,2,3   To not break the program we -1)
    output = ""
    objects = ["` ", "@ ", "R ", "F ", "# "] # This list is the characters we display. The space in each one is to keep them spaced out when printed.

    for _ in range(Grid): # Grid is the total size of the grid. This is to not go farther than we have places for a list. Stopping any Errors.
        point = MapArray2D[x][y] # the point is the current state of the position we are scanning.
        output += objects[point] # we take that point and use it as an index to our `objects` list. If the point is 0. Then it will add objects[0] which is " ` " 
        
        if x == (Offset - 1):   # Once we loop through the first line on the grid
                                # Offset -1 to not cause list errors
            x = 0 # Reset the scan position to 0
            y -= 1 # Go down the Y list by 1
            output += "\n" # Since we are at the end of our first line on the gird. We add "\n" to it. 
        else:
            x += 1 # If we haven't reached the end, continue.
    return output # Return the string

MapArray2D[1][1] = 1

while True: # Forever loop
    mapDisplay = UpdateDisplay(MapArray2D, GridSize, xGrid, yGrid)
    #time.sleep(1) # Loop every second
    print(mapDisplay) # Display list
    break #Comment this