import numpy as np
future_fish_records = np.zeros(7, dtype=np.longlong)
future_fish_dict = {}
def count_future_fishies(spawn_timer, total_days):
    sum = 1
    if(total_days < spawn_timer):
        return sum
    total_days_after_spawn = total_days-(spawn_timer+1)
    day_range = int((total_days_after_spawn) / 7)+1
    for x in reversed(range(day_range)):
        days_left = total_days_after_spawn-(x)*7
        days_left+=1
        #print ("total_days_after_spawn: " + str(total_days_after_spawn) + " spawn_timer: " + str(spawn_timer) + " days left: " + str(days_left) + " x: " + str(x) + " range:" + str(day_range))
        if days_left > 0:
            #print("total days: " + str(total_days) + " days left: " + str(days_left))
            key_string = "9," + str(days_left)
            if not key_string in future_fish_dict:              
                future_fish_dict[key_string] = count_future_fishies(9, days_left)
            sum += future_fish_dict[key_string]
    
    return sum
    

myfile = open("advent6.txt", "r")
myline = myfile.readline()

fishies = np.fromstring(myline,dtype=int,sep=',')

fish = 0
total_fish = 0
total_days = 256
for x in range(total_days):
    while fish < len(fishies):
        #print("fish starting num: " + str(fishies[fish]))
        if (future_fish_records[fishies[fish]] == 0):
            future_fish_records[fishies[fish]] = count_future_fishies(fishies[fish], total_days)
        total_fish += future_fish_records[fishies[fish]] 
        #print("future fish: " + str(future_fish_records[fishies[fish]]))
        fish += 1


print(total_fish)
