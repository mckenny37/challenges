import numpy as np

ten_signals = []
four_outputs = []


myfile = open("advent8.txt", "r")
myline = myfile.readline()
ctr = 0
while (myline):
    temp = myline.split("|")
    ten_signals.append(temp[0].strip().split(" "))
    four_outputs.append(temp[1].strip().split(" "))
    myline = myfile.readline()


#find 1, 4, 7, 8
ctr = 0
unique_nums = np.array([2,4,3,7])
for x in range(len(four_outputs)):
    for output in four_outputs[x]:
        if len(output) in unique_nums:
            ctr += 1

print(ctr)