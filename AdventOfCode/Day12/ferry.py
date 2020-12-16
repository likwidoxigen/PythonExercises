import math
finput ='./AdventOfCode/Day12/invalid.txt'
finput = './AdventOfCode/Day12/valid.txt'
finput = './AdventOfCode/Day12/Input.txt'

directions = []
cardinalsR = ['E','S','W','N']
cardinalsL = ['E','N','W','S']
def parseDirections(line):
    command = line[0:1]
    distance = int(line[1:])
    return {'command':command, 'distance':distance}

with open(finput, 'r') as file:
    lines = file.readlines()
    temp =""
    count = 0
    for line in lines:
        line =line.strip()
        if len(line) > 0:
            directions.append(parseDirections(line))

def rotateLeft(loc,repeat):
    newWY = loc['WX']
    newWX = -1*loc['WY'] 
    loc['WX'] = newWX
    loc['WY'] = newWY
    repeat -=1
    if repeat == 0:
        return loc
    else:
        return rotateLeft(loc,repeat)

def rotateRight(loc,repeat):
    newWY = -1*loc['WX']
    newWX = loc['WY'] 
    loc['WX'] = newWX
    loc['WY'] = newWY
    repeat -=1
    if repeat == 0:
        return loc
    else:
        return rotateRight(loc,repeat)

def updateWayPointRotation(loc,command):
    dirr = command['command']
    rotation = command['distance']
    numRotates = int(rotation/90)
    loc['WX'] = loc['WX'] + (-1*loc['X'])
    loc['WY'] = loc['WY'] + (-1*loc['Y'])
    print("_--MEMEMEMEM---------------")
    print(loc)
    if dirr == 'L':
        loc = rotateLeft(loc,numRotates)
    else:
        loc = rotateRight(loc,numRotates)
    print("_---secsecec-------")
    print(loc)

    loc['WX'] = loc['WX'] + (loc['X'])
    loc['WY'] = loc['WY'] + (loc['Y'])
    print("_---finfinfind-------")
    print(loc)
    return loc

def updateRotation(loc,command):
    cardinals = []
    pointing = loc['forward']
    dirr = command['command']
    rotation = command['distance']
    if dirr == 'L':
        cardinals = cardinalsL
    else:
        cardinals = cardinalsR
    start = cardinals.index(pointing)
    addOn = start + int(rotation/90)
    if addOn >= 4:
        addOn = addOn - 4
    #print(f"Command:{dirr}|Amount{rotation}|Started:{pointing}|Now:{cardinals[addOn]}")
    loc['forward'] = cardinals[addOn]
    return loc

def getNewLoc(loc,direction):
    if direction['command'] == 'N':
        loc['Y'] += direction['distance']
    if direction['command'] == 'S':
        loc['Y'] -= direction['distance']
    if direction['command'] == 'E':
        loc['X'] += direction['distance']
    if direction['command'] == 'W':
        loc['X'] -= direction['distance']
    if direction['command'] == 'F':
        direction['command'] = loc['forward']
        return getNewLoc(loc,direction)
    if direction['command'] == 'L' or direction['command'] == 'R':
        return updateRotation(loc,direction)
    return loc

def getNewLoc2(loc,direction):
    if direction['command'] == 'N':
        loc['WY'] += direction['distance']
    if direction['command'] == 'S':
        loc['WY'] -= direction['distance']
    if direction['command'] == 'E':
        loc['WX'] += direction['distance']
    if direction['command'] == 'W':
        loc['WX'] -= direction['distance']
    if direction['command'] == 'F':
        ychange = loc['WY'] + -1*loc['Y']
        xchange = loc['WX'] + -1*loc['X']
        print(f"ychange:{ychange}|xchange:{xchange}")
        loc['Y'] += (ychange) * direction['distance']
        loc['X'] += (xchange)  * direction['distance']
        loc['WY'] = (loc['Y'] + ychange)
        loc['WX'] = (loc['X'] + xchange)

    if direction['command'] == 'L' or direction['command'] == 'R':
        return updateWayPointRotation(loc,direction)
    return loc

location = {'X':0, 'Y':0, 'WX':10, 'WY':1, 'forward':'E'}

directions2 = []
for direction in directions:
    directions2.append(direction.copy())
    location = getNewLoc(location,direction)

print(location)
print(f"Manhattan Distance:{abs(location['X']) + abs(location['Y'])}")

location = {'X':0, 'Y':0, 'WX':10, 'WY':1, 'forward':'E'}

print(location)
for direction in directions2:
    location = getNewLoc2(location,direction)
    print(location)


print("---------------------------")
print(location)
print(f"Manhattan Distance:{abs(location['X']) + abs(location['Y'])}")
