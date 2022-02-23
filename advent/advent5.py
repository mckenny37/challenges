map = {}
def order_pair(first,second):
    if(first > second):
        return second,first
    else:
        return first,second
def add_pairs(c_pairs):
    #print(c_pairs)
    if c_pairs[0] == c_pairs[2]:
        y1,y2=order_pair(c_pairs[1],c_pairs[3])
        for y in range (y1,y2+1):
            add_points(c_pairs[0], y)
            #print(y)
    elif c_pairs[1] == c_pairs[3]:
        x1,x2=order_pair(c_pairs[0],c_pairs[2])
        for x in range (x1,x2+1):
            #print(x)
            add_points(x, c_pairs[1])
    elif (c_pairs[2]-c_pairs[0])==(c_pairs[3]-c_pairs[1]):
        y1,y2=order_pair(c_pairs[1],c_pairs[3])
        x1,x2=order_pair(c_pairs[0],c_pairs[2])
        while x1 <= x2:
            add_points(x1,y1)
            x1+=1
            y1+=1
    elif abs(c_pairs[2]-c_pairs[0])==abs(c_pairs[3]-c_pairs[1]):
        print(c_pairs)
        if(c_pairs[2]>c_pairs[0]):
            y = c_pairs[1]
            for x in range(c_pairs[0],c_pairs[2]+1):
                print("x: " + str(x) + " y: " + str(y))
                add_points(x,y)
                y -= 1
        else:
            y = c_pairs[3]
            for x in range(c_pairs[2],c_pairs[0]+1):
                print("x: " + str(x) + " y: " + str(y))
                add_points(x,y)
                y -= 1

def add_points(x,y):  
    if x in map: 
        if y in map[x]:
            map[x][y] += 1
        else:
            map[x][y] = 1
    else:
        map[x] = {}
        map[x][y] = 1

myfile = open("advent5.txt", "r")
myline = myfile.readline()
coordinates = []

while myline:
    c_pair = [int(n) for n in myline.replace(" -> ",",").strip().split(",")]
    coordinates.append(c_pair)
    myline = myfile.readline()
myfile.close()

for c_pairs in coordinates:
    add_pairs(c_pairs)

sum = 0
for row in map:
    row_str = ""
    for column in map[row]:
        row_str += str(map[row][column])
        if map[row][column] > 1:
            sum += 1
    #print(row_str)
print(sum)