import re


passports = []
finput = './AdventOfCode/Day04/valid.txt'
finput ='./AdventOfCode/Day04/invalid.txt'
finput = './AdventOfCode/Day04/Input.txt'


with open(finput, 'r') as file:
    lines = file.readlines()
    tmp = {}
    for line in lines:
        line = line.strip()
        if len(line) < 3:
            passports.append(tmp)
            tmp = {}
        else:
            for item in line.split(' '):
                tmp[item.split(":")[0]] = item.split(":")[1]
    passports.append(tmp)


valid_passports = 0
def check_passport(passport):
    required_fields = ['byr','iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for reqd in required_fields:
        if reqd not in passport:
            return False
        if validData(reqd,passport[reqd]) == False:
            return False
    print(passport)
    return True

def validData (reqd, data):
    try:
        if reqd == "byr":
            if len(str(data)) != 4 or int(data) < 1920 or  int(data) > 2002:
                return False
        elif reqd == "iyr":
            if len(str(data)) != 4 or int(data) < 2010 or  int(data) > 2020:
                return False
        elif reqd == "eyr":
            if len(str(data)) != 4 or int(data) < 2020 or  int(data) > 2030:
                return False
        elif reqd == "ecl":
            if data not in ['amb','blu','brn','gry','grn','hzl','oth']:
                return False
        elif reqd == "pid":
            if len(data) != 9:
                return False
            test = int(data)
        elif reqd == "hcl":
            valid_hair = re.compile("^#[a-f0-9]{6}$")
            if (not re.search(valid_hair,data)):
                return False
        elif reqd == "hgt":
            if 'cm' in data:                
                data = int(data[0:-2])
                if data < 150 or data > 193:
                    return False
            else:
                data = int(data[0:-2])
                if data < 59 or data > 76:
                    return False
    except:
        return False
    return True

for passport in passports:
    if check_passport(passport) == True:
        valid_passports += 1

print(len(passports))
print(valid_passports)