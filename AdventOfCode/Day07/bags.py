finput ='./AdventOfCode/Day07/invalid.txt'
finput = './AdventOfCode/Day07/valid.txt'
finput = './AdventOfCode/Day07/Input.txt'


bags = []
bagDict = {}
def parseBag(line):
    bagray = line.split(' contain ')
    return {'name':bagray[0][0:-1], 'contains':bagray[1]}

def addBag(line):
    bagray = line.replace("bags","bag").split(' contain ')
    #print(bagray[0][0:-1])
    bagDict[bagray[0]] = bagray[1][0:-1]

with open(finput, 'r') as file:
    lines = file.readlines()
    temp =""

    count = 0
    for line in lines:
        line =line.strip()
        if len(line) >= 2:
            addBag(line)
            bags.append(parseBag(line))

count = 0
currentCount=1
findBag = ""
bagSearch = ['shiny gold bag']
allBags = []
while (len(bagSearch) >= 1):
    try:
        findBag = bagSearch.pop()
    except:
        bagSearch=[]
        findBag=""
    for x in bags:
        if findBag in x['contains']:
            #print(x['name'])
            currentCount += 1
            bagSearch.append(x['name'])
            allBags.append(x['name'])
allBags = list(dict.fromkeys(allBags))
print(len(allBags))


totalBags = 0
def getBagCount(numBags, bagSearchString):
    bagSearch = bagDict[bagSearchString].split(", ")
    bar=0
    #print(bagSearch[0])
    if bagSearch[0] == 'no other bag':
        #print(numBags)
        return numBags
    for x in bagSearch:
        subCount = int(x.split(' ')[0])
        bagName = ' '.join(x.split(' ')[1:])
        bar += getBagCount(subCount,bagName)
        #print(f"|{subCount}|{bagName}|{bar}|")
    print(f"{numBags}*{bar}")
    return numBags*bar +numBags

totalBags = getBagCount(1,'shiny gold bag')
print(totalBags-1)