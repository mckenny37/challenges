myfile = open("advent3.txt", "r")
binary = myfile.readlines()
myfile.close()
myfile = open("advent3.txt", "r")
binary2 = myfile.readlines()
myfile.close()

values = {}
for x in binary:
    #print(x)
    for index in range(0, len(x)-1):
        #print(index)
        if x[index] == "1":
            value = 1
        else:
            value = -1
        #print(value)
        if index in values:
            values[index] += value
        else:
            values[index] = value

gamma = ""
epsilon = ""
print(values)
for x in values:
    if values[x] > 0:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

def convert_binary(binary):
    decimal = 0
    #apparently we have to go past 0 to -1, for index to go down to 0
    for index in range(len(binary)-1,-1,-1):
        binary_index_val = int(binary[index])*2**((len(binary)-1)-(index))
        decimal += binary_index_val
        print(str(index) + ": " + str(binary_index_val))
    return decimal

print ("gamma: " + gamma)
print ("epsilon: " + epsilon)
gamma_dec = convert_binary(gamma)
epsilon_dec = convert_binary(epsilon)
print ("gamma_dec: " + str(gamma_dec))
print ("epsilon_dec: " + str(epsilon_dec))
print (gamma_dec*epsilon_dec)


sum = 0
oxygen = ""
co2 = ""
for index in range(0,len(binary[0])):
    for x in binary:
        if x[index] == "1":
            value = 1
        else:
            value = -1
        sum += value
    if sum < 0:
        value = "0"
    else:
        value = "1"

    sum = 0
    del_indices = []
    for bin_index in range(0,len(binary)):
        if binary[bin_index][index] != value:
            #print (bin_index)
            del_indices.append(bin_index)
    
    for y in reversed(del_indices):
        #print(y)
        del binary[y]
    
    if len(binary) == 1:
        oxygen = binary[0].strip('\n')


sum = 0
binary = binary2
for index in range(0,len(binary[0])):
    print_bool = False
    for x in binary:
        if x[index] == "1":
            value = 1
        else:
            value = -1
        sum += value
    if sum >= 0:
        value = "0"
    else:
        value = "1"

    sum = 0

    del_indices = []
    for bin_index in range(0,len(binary)):
        if binary[bin_index][index] != value:
            if print_bool:
                print("value: " + value + " index: " + index + " binary: " + binary[bin_index])
            del_indices.append(bin_index)
    
    for y in reversed(del_indices):
        #print(y)
        del binary[y]
    
    if len(binary) < 10:
        print_bool = True
        print(binary)
        print(index)
    if len(binary) == 1:
        co2 = binary[0].strip('\n')

print("oxygen: " + str(oxygen))
print("co2: " + co2)
oxygen_dec = convert_binary(oxygen)
co2_dec = convert_binary(co2)
print ("oxygen_dec: " + str(oxygen_dec))
print ("co2_dec: " + str(co2_dec))
print(co2_dec * oxygen_dec)