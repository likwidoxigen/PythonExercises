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

def updateWayPointRotation(loc,command):
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
    if loc['forward'] == 'N':
        # ! -1 1
        loc['WX'] = loc['WX'] if loc['WX'] < 0 else loc['WX'] * -1
        loc['WY'] = abs(loc['WY'])
    elif loc['forward']== 'E':
        loc['WX'] = abs(loc['WX'])
        loc['WY'] = abs(loc['WY'])
        # ! 1 1
    elif loc['forward'] == 'W':
        # ! -1 1
        loc['WX'] = loc['WX'] if loc['WX'] < 0 else loc['WX'] * -1
        loc['WY'] = loc['WY'] if loc['WY'] < 0 else loc['WY'] * -1
    else:
        # ! -1 -1
        loc['WX'] = abs(loc['WX'])
        loc['WY'] = loc['WY'] if loc['WY'] < 0 else loc['WY'] * -1
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
        loc['Y'] += (loc['WY'] * direction['distance'])
        loc['X'] += (loc['WX'] * direction['distance'])
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

for direction in directions2:
    location = getNewLoc2(location,direction)

print(location)
print(f"Manhattan Distance:{abs(location['X']) + abs(location['Y'])}")