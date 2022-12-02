
data = []
calledNumbers = []

def process_input(line):
    global calledNumbers, data
    if len(line) >0 and len(line) < 20:
            data.append(line.split())
    elif len(line) > 20:
            calledNumbers = line.split(',')

def load_data(filename):
    with open (filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            process_input(line.strip())

def partA():
    global calledNumbers, data
    print(calledNumbers)

def partB():
    global calledNumbers, data
    print(data)
    bingo_printer(data,0)

def bingo_checker(data,start):
    print("in Process")

def check_verticals(data,start):
    print("todo")
def check_horizontal(data,start):
    print("todo")
def check_diagonals(data,start):
    print("todo")

def bingo_printer(data2,start):
    end = start + 5
    while start < end:
        bstring=""
        for item in data2[start]:
            bstring += f"{int(item):02} "
        print(bstring.strip())
        start += 1


def main():
    inputfile = "./input01a.txt"
    inputfile = "./sample.txt"
    load_data(inputfile)
    partA()
    partB()
main()