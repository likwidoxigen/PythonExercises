map = []
maxWindex = 0

with open('./AdventOfCode/Day03/Input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        map.append(list(line.strip()))

def getNextWidth(num):
    if num > maxWindex:
        return num-maxWindex-1
    else:
        return num

maxWindex = len(map[0])-1
def splatCount(right,down):
    x=0
    count = 0
    for y in range(down,len(map),down):
        x = getNextWidth(x+right)
        #print(f"x{x} Y{y} map:{map[y][x]}")
        if map[y][x] == '#':
            count +=1
    return count
#3,1 better equal 198
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
#slopes = [[3,1]]
splatCounter = 1

for slope in slopes:
    print(f"{slope}: {splatCount(slope[0],slope[1])}")
    splatCounter*=splatCount(slope[0],slope[1])
print(splatCounter)