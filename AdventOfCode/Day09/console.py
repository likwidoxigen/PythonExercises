finput ='./AdventOfCode/Day09/invalid.txt'

finput = './AdventOfCode/Day09/Input.txt'
finput = './AdventOfCode/Day09/valid.txt'


xmas = []
global badValues
badValues = []
global checkArray
checkArray = []
preamble = 5
with open(finput, 'r') as file:
    lines = file.readlines()
    temp =""
    count = 0
    for line in lines:
        line =line.strip()
        if len(line) > 0:
            xmas.append(int(line))


def checkSum(checkhere, lenf, sum):
    if sum == 0:
        return True
    if (lenf == 0 and sum != 0 ):
        return False

    if (checkhere[lenf-1]> sum):
        return checkSum(checkhere,lenf-1,sum)
    
    return checkSum(checkhere,lenf-1,sum) or checkSum(checkhere,lenf-1,sum-checkhere[lenf-1])

for sum in xmas:
    if ( len(checkArray) < preamble ):
        checkArray.append(sum)
    else:
        print(f"{checkArray}_Sum:{sum}")
        if checkSum(checkArray,len(checkArray),sum):
            print(f"sum Found for:{sum}")
        else:
            badValues.append(sum)
        del checkArray[0]
        checkArray.append(sum)

print("We have failed for: ")
for x in badValues:
    print(x)