
data = []

def process_input(line):
    if len(line) >0:
        tokens = line.split(' ')
        data.append({"direction":""+tokens[0], "amount":int(tokens[1])})

def load_data(filename):
    with open (filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            process_input(line.strip())

def partA():
    hp = 0
    dp = 0
    for instruction in data:
        if instruction['direction'] == "up":
            dp -= instruction['amount']
        elif instruction['direction'] == "down":
            dp += instruction['amount']
        elif instruction['direction'] == "forward":
            hp += instruction['amount']
    print("hp:",hp," dp:",dp," ans:",hp*dp)


def partB():
    hp = 0
    dp = 0
    aim = 0
    for instruction in data:
        if instruction['direction'] == "up":
            aim -= instruction['amount']
        elif instruction['direction'] == "down":
            aim += instruction['amount']
        elif instruction['direction'] == "forward":
            hp += instruction['amount']
            dp +=  aim *  instruction['amount']
        # print("hp:",hp, " dp:",dp, " aim: ",aim)
    print("hp:",hp, " dp:",dp, " aim: ",aim, " ans:",hp*dp)

def main():
    inputfile = "./input01a.txt"
    # inputfile = "./sample.txt"
    load_data(inputfile)
    partA()
    partB()
main()