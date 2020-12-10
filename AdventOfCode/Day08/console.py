finput ='./AdventOfCode/Day08/invalid.txt'
finput = './AdventOfCode/Day08/valid.txt'
finput = './AdventOfCode/Day08/Input.txt'


instructions = []
global currentCommand
currentCommand = 0
global accumulator
accumulator = 0

with open(finput, 'r') as file:
    lines = file.readlines()
    temp =""
    count = 0
    for line in lines:
        line =line.strip()
        if len(line) >= 2:
            instructions.append(line)



def processCommand(lineNum):
    cmd = instructions[lineNum].split(" ")[0].strip()
    amt = int(instructions[lineNum].split(" ")[1].strip())
    global accumulator
    if 'acc' in cmd:
        accumulator = accumulator + amt
        return (lineNum + 1)
    elif 'jmp' in cmd:
        return lineNum + amt
    else:
        return lineNum + 1

def runProgram():
    global currentCommand
    global accumulator
    accumulator = 0
    currentCommand = 0
    runtime = []
    while ((currentCommand not in runtime) and currentCommand < len(instructions)):
        runtime.append(currentCommand)
        print(instructions[currentCommand])
        print(f"1not in runtime:{ currentCommand}")
        currentCommand = processCommand(currentCommand)
        print(f"2not in runtime:{ currentCommand}")
        print(f"curcmd less:{currentCommand < len(instructions)}")
        print(f"processing:{currentCommand}|{runtime}")
    print(accumulator)
    if (currentCommand not in runtime) and currentCommand == len(instructions):
        return True
    else:
        return False

changedCmdNum = 0
def changeCommand(changedCmdNum):
    if 'nop' in instructions[changedCmdNum]:
        instructions[changedCmdNum] = instructions[changedCmdNum].replace('nop','jmp')
        return True
    elif 'jmp' in instructions[changedCmdNum]:
        instructions[changedCmdNum]= instructions[changedCmdNum].replace('jmp','nop')
        return True
    else:
        return False

if runProgram():
    print("Success!")
else:
    print("Failure!")
firstRun = True
status = False
while (status == False and changedCmdNum < len(instructions)):
    status = runProgram()
    if status == False:
        print(f"Changed CMD Num:{changedCmdNum}")
        if (firstRun):
            firstRun= False
            changed = changeCommand(changedCmdNum)
            while not changed and changedCmdNum < len(instructions):
                changed = changeCommand(changedCmdNum)
                if changed == False:
                    changedCmdNum +=1
        else:
            changeCommand(changedCmdNum)
            changedCmdNum+=1
            changed = changeCommand(changedCmdNum)
            while not changed and changedCmdNum < len(instructions):
                changed = changeCommand(changedCmdNum)
                if changed == False:
                    changedCmdNum +=1

# for x in instructions:
#     print(x)
# print(f"Acc:{accumulator}")               
# print(f"Changed Command Number:{changedCmdNum}")


# while ((currentCommand not in runtime) and lineNum < len(instructions)):
