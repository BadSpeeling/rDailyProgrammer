import numpy

f = open("input.txt", "r")

dims = f.readline().split(" ")

row = int(dims[0])
col = int(dims[1])

amtWater = [[]]

for i in range(0,row):
    amtWater.append([0]*col)

del amtWater[0]

heights = [[]]

for i in range(0,row):
    line = f.readline()
    line = line.split(" ")
    for j in range(0,len(line)):
        line[j] = int(line[j])
    heights.append(line)

del heights[0]
target = int(f.readline())
targetRC = None
beginRC = None

for i in range(0,len(heights)):
    for j in range(0,len(heights[i])):
        if (heights[i][j] == target):
            targetRC = (i,j)
        elif (heights[i][j] == 1):
            beginRC = (i,j)
        
print targetRC
print beginRC
print amtWater