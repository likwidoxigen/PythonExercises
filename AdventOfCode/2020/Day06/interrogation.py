finput ='./AdventOfCode/Day06/invalid.txt'
finput = './AdventOfCode/Day06/valid.txt'
finput = './AdventOfCode/Day06/Input.txt'

questions =[]
questions2 = []

def getCountLetters(str):
    dct = {}
    for x in range(0,len(str)):
        try:
            dct[str[x]] += 1
        except:
            dct[str[x]] = 1
    return dct

def getAllSameCount(str, num_people):
    dct = getCountLetters(str)
    count = 0
    for key in dct:
        print(f"key:{dct[key]}  numPeople:{num_people}")
        if dct[key] == num_people:
            count += 1
    return count

with open(finput, 'r') as file:
    lines = file.readlines()
    temp =""
    count = 0
    for line in lines:
        line =line.strip()
        if len(line) >= 1:
            count += 1
            temp += line
        else:
            questions.append(len(dict.fromkeys(list(temp))))
            questions2.append(getAllSameCount(temp,count))
            temp = ""
            count = 0
    questions.append(len(dict.fromkeys(list(temp))))
    questions2.append(getAllSameCount(temp,count))

print(questions)
print(sum(questions))

print(questions2)
print(sum(questions2))