def index_2d(data, search):
    for i, e in enumerate(data):
        try:
            return i, e.index(search)
        except ValueError:
            pass
    raise ValueError("{!r} is not in list".format(search))

def check_bingo(data, position):
    data[0][position[0]] += 1
    data[1][position[1]] += 1
    if data[1][position[1]] == 5:
        print("vertical!")
        print(position)
        print(data[1])
    if data[0][position[0]] == 5 or data[1][position[1]] == 5:
        return True
    else:
        return False

def find_bingo(mynumbers, bingocards):  
    winningnum=0
    last_winning_card=-1 
    bingo_results = []
    for num in range(0,len(bingocards)):
        bingo_results.append([[0,0,0,0,0],[0,0,0,0,0]])
    ctr = 1
    for x in mynumbers:
        card = 0 
        while card < len(bingocards):
            if len(bingocards) < 3:
                print("current: " + str(card) + " left: " + str(len(bingocards)) + " currentnum: " + str(ctr) + " totalnum: " + str(len(mynumbers)))
            try:
                position = index_2d(bingocards[card], x)
                bingocards[card][position[0]][position[1]] = -1
                if check_bingo(bingo_results[card], position):
                    if len(bingocards) == 2:
                        return x, card
                    bingocards.pop(card)
                    bingo_results.pop(card)
                else:
                    card += 1
            except:
                card += 1
                continue
        ctr+=1
    return winningnum,last_winning_card

myfile = open("advent4.txt", "r")
mynumbers = myfile.readline().strip().split(",")
myline = myfile.readline()
bingocards = []
cardctr = 0
rowctr = 0
bingocards.insert(cardctr,[])

while myline:
    #print(myline)
    if myline.strip() == "":
        #print(cardctr)
        cardctr += 1
        bingocards.insert(cardctr,[])
    else:
        bingocards[cardctr].append(myline.split())
    myline = myfile.readline()
myfile.close()

num,cardnum = find_bingo(mynumbers,bingocards)

print(num)
print(cardnum)
print(bingocards[cardnum])

sum = 0
for x in range(0,5):
    for y in range(0,5):
        if int(bingocards[cardnum][x][y]) >= 0:
            sum += int(bingocards[cardnum][x][y])
            print(bingocards[cardnum][x][y])

print(sum)
print(sum*(int(num)))

#print(bingocards)