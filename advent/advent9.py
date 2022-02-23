import numpy as np
import heapq


map = []
def split(word):
    return [char for char in word]

def check_for_low_point(x,y):
    diff = [-1,1]
    for z in diff:
        if(check_lower_value(map[x][y],x+z,y)):          
            return False
        if(check_lower_value(map[x][y],x,y+z)):
            return False
    return True
    
def check_lower_value(val,x,y):
    try: 
        retvalue = False
        if x >=0 and y >= 0 and x < len(map) and y < len(map[0]):
            if int(map[x][y]) <= int(val):            
                retvalue=True
    except: 
        print("exception")
        return False
    return retvalue

def discover_basin(x,y):
    sum = 1
    sum = discover_basin_recursion(x,y,-1,0)
    sum += discover_basin_recursion(x,y,1,0)
    sum += discover_basin_recursion(x,y,0,-1)
    sum += discover_basin_recursion(x,y,0,1)
    return sum

def discover_basin_recursion(x,y,x_inc,y_inc):
    try:
        if int(map[x][y])+1==int(map[x+x_inc][y+y_inc]):
                return 1 + discover_basin_recursion(x+x_inc,y+y_inc,x_inc,y_inc)
        else:
            return 0       
    except:
        return 0

myfile = open("advent9.txt", "r")
myline = myfile.readline()
ctr = 0
while (myline):
    temp = split(myline.strip())
    map.append(temp)
    myline = myfile.readline()

sum = 0
low_points = {}
basins = []

for x in range(len(map)):
    for y in range(len(map[0])):
        if check_for_low_point(x,y):
            sum += int(map[x][y]) + 1
            if x not in low_points:
                low_points[x] = {}
            low_points[x][y] = 1

for x in low_points:
    for y in low_points[x]:
        #start_with value-1 in order to start calculating basin at actual starting point
        heapq.heappush(basins,discover_basin(x,y))

print(basins)
