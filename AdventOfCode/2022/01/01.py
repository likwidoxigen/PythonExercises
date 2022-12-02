curr = 0
maxcals = 0
data = []

def process_input(line):
    global maxcals, curr, data
    if len(line) >0:
            curr += int(line)
    else:
        data.append(curr)
        curr = 0

def load_data(filename):
    global data, curr
    with open (filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            process_input(line.strip())
    data.append(curr)

def partA():
    global data
    print("Part A")
    print(max(data))

def partB():
    global data
    print("Part B")
    sorted = data.sort()
    print(sum(data[-3:]))
    

def main():
    inputfile = "./input01a.txt"
    #inputfile = "./sample.txt"
    load_data(inputfile)
    
    partA()
    partB()
main()