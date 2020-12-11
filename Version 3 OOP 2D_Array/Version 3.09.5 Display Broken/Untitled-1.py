xGrid = 5
yGrid = 5
GridSize = xGrid * yGrid

MapArray2D = [[0 for i in range(yGrid)] for j in range(xGrid)]

def UpdateDisplay(MapArray2D):
    output = ""
    objects = ["` ", "@ ", "R ", "F ", "# "]
    TempList = MapArray2D
    TempList.reverse()

    for i in TempList:
        for j in i:
            output += objects[j]
        output += "\n"
    
    print(output)

UpdateDisplay(MapArray2D)