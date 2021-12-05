
data = []

def process_input(line):
    if len(line) >0:
        data.append(int(line.strip()));

def load_data(filename):
    with open (filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            process_input(line)

def partA():
    numDiffs = 0
    compdict = {"previous": -1, "current": -1}
    for val in data:     
        compdict['previous'] = compdict['current']
        compdict['current'] = val
        if ( compdict['previous'] != -1 and compdict['current'] - compdict['previous'] >=1):
            numDiffs += 1
    print (numDiffs)


def partB():
    index = 0
    numDiffs = 0
    data2 = data.copy()
    while index +3 < len(data2):
        listA = data[index:index+3]
        listB=  data[index+1:index+4]
        # if index == 0:
        #     print("listA:",listA,sum(listA))
        # else:
        #     print("listB:",listB,sum(listB))
        difference = sum(listB) - sum(listA)
        if ( difference >0):
            numDiffs += 1
        index +=1
    print(numDiffs)

def main():
    inputfile = "./input01a.txt"
    # inputfile = "./sample.txt"
    load_data(inputfile)
    partA()
    partB()
main()