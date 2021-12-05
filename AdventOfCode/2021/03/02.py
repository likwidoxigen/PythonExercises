
data = []
dlength = 0

def process_input(line):
    global dlength, data
    if len(line) >0:
        dlength = len(line)
        data.append(list(line))

def load_data(filename):
    with open (filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            process_input(line.strip())

def position_sum(data2,index):
    sum = 0
    for val in data2:
        sum += int(val[index])
    return int(sum)

def get_rates(sums, inputLength):
    gamma = []
    epsilon = []
    for x in sums:
        if x > inputLength/2:
            gamma.append(1)
            epsilon.append(0)
        else:
            gamma.append(0)
            epsilon.append(1)
    print(''.join(map(str,gamma)))
    print(''.join(map(str,epsilon)))
    print("gamma:", int(''.join(map(str,gamma)),2))
    print("epsilon:", int(''.join(map(str,epsilon)),2))
    return {"gamma":gamma, "epsilon":epsilon}

def partA():
    global dlength, data
    index = 0
    inputLength=len(data)
    sums = []
    while index < dlength:
        sums.append(position_sum(data,index))
        index += 1
    print("Data length:",dlength ," Input Length:",inputLength)
    print("sums: ",sums)
    ge = get_rates(sums, inputLength)

def getSubList(list,index,value):
    subList = [];
    for val in list:
        if int(val[index]) == int(value):
            subList.append(val)
    return subList

def oxygenGenerator():
    data2 = data.copy()
    index = 0
    while len(data2) > 1 and index<dlength:
        if position_sum(data2,index ) >=  (len(data2)/2):
            most_common = 1
        else:
            most_common = 0
        # print("most_common:",most_common, "index: ",index)
        data2 = getSubList(data2,index,most_common)
        index+=1
    print("oxygen Generator: ", int(''.join(map(str,data2[0])),2))

def coScrubber():
    data2 = data.copy()
    index = 0
    while len(data2) > 1 and index<dlength:
        if position_sum(data2,index ) <  (len(data2)/2):
            most_common = 1
        else:
            most_common = 0
        # print("most_common:",most_common, "index: ",index)
        data2 = getSubList(data2,index,most_common)
        index+=1
    print("Co2 Scrubber: ", int(''.join(map(str,data2[0])),2))

def partB():
    oxygenGenerator()
    coScrubber()

def main():
    inputfile = "./input01a.txt"
    # inputfile = "./sample.txt"
    load_data(inputfile)
    partA()
    partB()
main()