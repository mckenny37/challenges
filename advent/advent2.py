myfile = open("advent2.txt", "r")
depths = myfile.readlines()
ctr = 0
values = {
    'forward':0,
    'up':0,
    'down':0,
    'depth':0
}
for x in depths:
    print(x)
    split = x.split(" ")
    if split[0] == "forward":        
        values['depth'] += int(split[1])*(values['down']-values['up'])
    values[split[0]] += int(split[1])

print(values)
print(values["forward"] * values["depth"])