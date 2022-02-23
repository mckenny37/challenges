import numpy as np
fish_lives = np.zeros(9, dtype=np.longlong)


myfile = open("advent6.txt", "r")
myline = myfile.readline()

fishies = np.fromstring(myline,dtype=int,sep=',')
for fish in fishies:
    fish_lives[fish] +=1

print(fish_lives)

for x in range(256):
    new_fish = fish_lives[0]     
    for spawn_time in range(len(fish_lives)):
        if spawn_time==8:
            fish_lives[6] += new_fish
            fish_lives[8] = new_fish
        else:
            fish_lives[spawn_time] = fish_lives[spawn_time+1]
            fish_lives[spawn_time+1] = 0
    print(fish_lives)
print(fish_lives.sum())