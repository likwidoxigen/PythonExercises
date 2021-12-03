finput ='./AdventOfCode/Day09/invalid.txt'
finput = './AdventOfCode/Day09/valid.txt'
finput = './AdventOfCode/Day09/Input.txt'



xmas = []
global badValues
badValues = []
global checkArray
checkArray = []
preamble = 25
with open(finput, 'r') as file:
    lines = file.readlines()
    temp =""
    count = 0
    for line in lines:
        line =line.strip()
        if len(line) > 0:
            xmas.append(int(line))


def checkSum(checkhere, lenf, sum,count):
    if ( count > 2 ):
        return False
    if ( sum == 0 ):
        return True
    if (lenf == 0 and sum != 0 ):
        return False

    if (checkhere[lenf-1]> sum):
        return checkSum(checkhere,lenf-1,sum, count)
    
    return checkSum(checkhere,lenf-1,sum,0) or checkSum(checkhere,lenf-1,sum-checkhere[lenf-1],count+1)

for sum in xmas:
    if ( len(checkArray) < preamble ):
        checkArray.append(sum)
    else:
        #print(f"{checkArray}_Sum:{sum}")
        if checkSum(checkArray,len(checkArray),sum,0):
            #print(f"sum Found for:{sum}")
            sum
        else:
            badValues.append(sum)
        del checkArray[0]
        checkArray.append(sum)

print("We have failed for: ")
for x in badValues:
    print(x)

badValue = badValues.pop()

def sumItUp(numbers):
    sum = 0
    for x in numbers:
        sum +=x
    return sum

keepGoing = True
start =0
end = 0
for x in range(len(xmas)):
    start=x
    end=x+1
    sum = sumItUp(xmas[start:end])
    while sum < badValue and end < len(xmas):
        end += 1
        sum = sumItUp(xmas[start:end])
    
    if sum == badValue:
        print(f"Start:{start},End:{end}")
        break

print(f"Start:{start},End:{end}")
print(f"Min:{min(xmas[start:end])}\nMax:{max(xmas[start:end])}")
print(f"Sum:{min(xmas[start:end])+max(xmas[start:end])}")


