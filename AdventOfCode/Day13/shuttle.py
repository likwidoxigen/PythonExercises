
finput ='./AdventOfCode/Day13/invalid.txt'
finput = './AdventOfCode/Day13/valid.txt'
finput = './AdventOfCode/Day13/Input.txt'


busStuff= []
time = 0
bus2 = {}
with open(finput, 'r') as file:
    lines = file.readlines()
    temp =""
    count = 0
    time = int(lines.pop(0).strip())
    lines = lines.pop().strip().split(",")
    timeStamp = 0
    for line in lines:
        line =line.strip()
        if line == 'x':
            timeStamp+=1
        else:
            bus2[timeStamp] = int(line)
            timeStamp+=1
        if len(line) > 0 and line != 'x':
            busStuff.append(int(line))
busStuff.sort()
print(f"Time:{time}|{busStuff}")

keepGoing = True
closestBus = 0
timeCheck = time
while keepGoing:
    for x in busStuff:
        # print(f"{float(timeCheck) % float(x)}")
        if float(timeCheck) % float(x) == 0:
            keepGoing = False
            closestBus = x
    timeCheck += 1

timeCheck-=1
print(f"Time:{timeCheck-time}|Bus:{closestBus}|Product:{(timeCheck-time)*closestBus}")

minbus = min(busStuff)
timeCheck = max(busStuff) * min(busStuff)
keepGoing = True
while keepGoing:
    mod =0
    found =[]
    for x in bus2:
        if (timeCheck +x) % bus2[x] != 0:
            break
        else:
            found.append(x)
    if (len(found) == len(bus2)):
        keepGoing = False
    timeCheck+=minbus
timeCheck -= minbus
print(f"Time:{timeCheck}")