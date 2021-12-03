pws = []
def parsePW(line):
    policy,pw = line.split(":")
    pw = pw.strip()
    policy,letter = policy.split(' ')
    min = int(policy.split("-")[0])-1
    max = int(policy.split("-")[1])-1
    
    return {'min':min, 'max':max, 'letter':letter, 'pw':pw}

def checkPW(pw):
    count = 0
    for i in pw['pw']:
        if i ==  pw['letter']:
            count +=1
    if count >= pw['min'] and count<= pw['max']:
        return True
    else:
        return False

def checkPW2(pw):
    strist = list(pw['pw'])
    try:
        if (strist[pw['min']] ==  pw['letter']) ^ (strist[pw['max']] ==  pw['letter']):
            return True
        else:
            return False
    except IndexError:
        return False



with open('./AdventOfCode/Day02/Input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        pws.append(parsePW(line))

count = 0
for pw in pws:
    if checkPW2(pw) == True:
        count+=1
print(count)