myfile = open("advent1.txt", "r")
myline = myfile.readline()
depths = []
ctr = 0

while myline:
  current = int(myline)
  depths.append(current)
  myline = myfile.readline()
myfile.close()

for x in range(3,len(depths)):
  current = depths[x] + depths[x-1] + depths[x-2]
  prev = depths[x-1] + depths[x-2] + depths[x-3]
  if current > prev:
    ctr+=1
print(ctr)
