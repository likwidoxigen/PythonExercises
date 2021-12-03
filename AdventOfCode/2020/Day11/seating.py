finput ='./AdventOfCode/Day11/invalid.txt'
finput = './AdventOfCode/Day11/valid.txt'
finput = './AdventOfCode/Day11/Input.txt'



seats = []
with open(finput, 'r') as file:
    lines = file.readlines()
    temp =""
    count = 0
    for line in lines:
        line =line.strip()
        if len(line) > 0:
            seats.append(list(line))

def isOccupied(arr,x,y):
    if arr[y][x] == "#":
        return 1
    else:
        return 0

def isOccupied2(arr,x,y):
    if arr[y][x] == "#":
        return 1
    elif arr[y][x] == "L":
        return 0
    else:
        return 5

def checkDownLeft(arr,x,y):
    x = x-1
    y = y-1
    if x < 0 or x > len(arr[0])-1 or y > len(arr)-1 or y < 0:
        return 0
    else:
        return isOccupied(arr,x,y)

def checkDownLeft2(arr,x,y):
    x = x-1
    y = y-1
    if x < 0 or x > len(arr[0])-1 or y > len(arr)-1 or y < 0:
        return 0
    else:
        test =  isOccupied2(arr,x,y)
        if test == 5:
            return checkDownLeft2(arr,x,y)
        else:
            return test

def checkLeft(arr,x,y):
    x = x-1
    y = y
    if x < 0 or x > len(arr[0])-1 or y > len(arr)-1 or y < 0:
        return 0
    else:
        return isOccupied(arr,x,y)

def checkLeft2(arr,x,y):
    x = x-1
    y = y
    if x < 0 or x > len(arr[0])-1 or y > len(arr)-1 or y < 0:
        return 0
    else:
        test =  isOccupied2(arr,x,y)
        if test == 5:
            return checkLeft2(arr,x,y)
        else:
            return test

def checkUpLeft(arr,x,y):
    x = x-1
    y = y+1
    if x < 0 or x > len(arr[0])-1 or y > len(arr)-1 or y < 0:
        return 0
    else:
        return isOccupied(arr,x,y)

def checkUpLeft2(arr,x,y):
    x = x-1
    y = y+1
    if x < 0 or x > len(arr[0])-1 or y > len(arr)-1 or y < 0:
        return 0
    else:
        test =  isOccupied2(arr,x,y)
        if test == 5:
            return checkUpLeft2(arr,x,y)
        else:
            return test

def checkUP(arr,x,y):
    x = x
    y = y+1
    if x < 0 or x > len(arr[0])-1 or y > len(arr)-1 or y < 0:
        return 0
    else:
        return isOccupied(arr,x,y)

def checkUP2(arr,x,y):
    x = x
    y = y+1
    if x < 0 or x > len(arr[0])-1 or y > len(arr)-1 or y < 0:
        return 0
    else:
        test =  isOccupied2(arr,x,y)
        if test == 5:
            return checkUP2(arr,x,y)
        else:
            return test

def checkDownRight(arr,x,y):
    x = x+1
    y = y-1
    if x < 0 or x > len(arr[0])-1 or y > len(arr)-1 or y < 0:
        return 0
    else:
        return isOccupied(arr,x,y)

def checkDownRight2(arr,x,y):
    x = x+1
    y = y-1
    if x < 0 or x > len(arr[0])-1 or y > len(arr)-1 or y < 0:
        return 0
    else:
        test =  isOccupied2(arr,x,y)
        if test == 5:
            return checkDownRight2(arr,x,y)
        else:
            return test

def checkRight(arr,x,y):
    x = x+1
    y = y
    if x < 0 or x > len(arr[0])-1 or y > len(arr)-1 or y < 0:
        return 0
    else:
        return isOccupied(arr,x,y)

def checkRight2(arr,x,y):
    x = x+1
    y = y
    if x < 0 or x > len(arr[0])-1 or y > len(arr)-1 or y < 0:
        return 0
    else:
        test =  isOccupied2(arr,x,y)
        if test == 5:
            return checkRight2(arr,x,y)
        else:
            return test

def checkUpRight(arr,x,y):
    x = x+1
    y = y+1
    if x < 0 or x > len(arr[0])-1 or y > len(arr)-1 or y < 0:
        return 0
    else:
        return isOccupied(arr,x,y)

def checkUpRight2(arr,x,y):
    x = x+1
    y = y+1
    if x < 0 or x > len(arr[0])-1 or y > len(arr)-1 or y < 0:
        return 0
    else:
        test =  isOccupied2(arr,x,y)
        if test == 5:
            return checkUpRight2(arr,x,y)
        else:
            return test


def checkDown(arr,x,y):
    x = x
    y = y-1
    if x < 0 or x > len(arr[0])-1 or y > len(arr)-1 or y < 0:
        return 0
    else:
        return isOccupied(arr,x,y)

def checkDown2(arr,x,y):
    x = x
    y = y-1
    if x < 0 or x > len(arr[0])-1 or y > len(arr)-1 or y < 0:
        return 0
    else:
        test =  isOccupied2(arr,x,y)
        if test == 5:
            return checkDown2(arr,x,y)
        else:
            return test

def checkSeat1(arr,x,y):
    currentSeat = arr[y][x]
    
    totalOccupied = (checkDownLeft(arr,x,y) +
        checkLeft(arr,x,y) + checkUpLeft(arr,x,y) + checkUP(arr,x,y) +
        checkDownRight(arr,x,y) + checkRight(arr,x,y) + checkUpRight(arr,x,y) + checkDown(arr,x,y) )
    
    if currentSeat == "L" and totalOccupied == 0:
        return "#"
    elif currentSeat == "#" and totalOccupied >= 4:
        return "L"
    else:
        return currentSeat

def checkSeat2(arr,x,y):
    currentSeat = arr[y][x]
    
    totalOccupied = (checkDownLeft2(arr,x,y) +
        checkLeft2(arr,x,y) + checkUpLeft2(arr,x,y) + checkUP2(arr,x,y) +
        checkDownRight2(arr,x,y) + checkRight2(arr,x,y) + checkUpRight2(arr,x,y) + checkDown2(arr,x,y) )
    
    if currentSeat == "L" and totalOccupied == 0:
        return "#"
    elif currentSeat == "#" and totalOccupied >= 5:
        return "L"
    else:
        return currentSeat

def checkSeats(arr1):
    newArry = copyArray(arr1)
    newArry = []
    row = []
    for y in range(len(arr1)):
        for x in range(len(arr1[y])):
            row.append(checkSeat1(arr1,x,y))
        newArry.append(row)
        row = []
    return newArry

def checkSeats2(arr1):
    newArry = copyArray(arr1)
    newArry = []
    row = []
    for y in range(len(arr1)):
        for x in range(len(arr1[y])):
            row.append(checkSeat2(arr1,x,y))
        newArry.append(row)
        row = []
    return newArry

def copyArray(arr1):
    arr2 = []
    for x in arr1:
        arr2.append(x.copy())
    return arr2

def countOccupied(arr1):
    sum =0
    for y in arr1:
        for x in y:
            if x =="#":
                sum+=1
    return sum

for x in range(132):
    seats = checkSeats2(seats)


for x in seats:
    print(''.join(x))

print(countOccupied(seats))