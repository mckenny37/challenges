import numpy as np

crab_fuel_rate = {}

def calc_crab_fuel(dist):
    if not dist in crab_fuel_rate:
        crab_fuel_rate[dist] = ((dist+1)*dist)//2
    return crab_fuel_rate[dist]


myfile = open("advent7.txt", "r")
crabs = np.fromstring(myfile.readline(),dtype=int,sep=',')

min = 9223372036854775807
for x in range(max(crabs)):
    sum = 0
    for crab in crabs:
        sum += calc_crab_fuel(abs(crab - x))
    if sum < min:
        min = sum


print(min)
