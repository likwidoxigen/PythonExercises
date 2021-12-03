def getMult2(charges):
    for x in charges:
        start = 0
        for y in range(start,len(charges)):
            if x+charges[y] == 2020:
                return x*charges[y]
        start +=1
        
def getMult3(charges):
    for x in charges:
        start = 0
        for y in range(start,len(charges)):
            if x+charges[y] < 2020:
                start2=start+1
                for z in range(start2,len(charges)):
                    if x+charges[y]+charges[z] == 2020:
                        return x*charges[y]*charges[z]
        start +=1

charges = []
with open('./AdventOfCode/Day1/Input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        charges.append(int(line))




print(getMult3(charges))