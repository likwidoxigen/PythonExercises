import math
finput = './AdventOfCode/Day10/valid.txt'

finput ='./AdventOfCode/Day10/valid2.txt'
finput = './AdventOfCode/Day10/Input.txt'

joltages = []
differences = []
# joltages.append(0) disabled to test timtim solution
with open(finput, 'r') as file:
    lines = file.readlines()
    temp =""
    count = 0
    for line in lines:
        line =line.strip()
        if len(line) > 0:
            joltages.append(int(line))


# This is Timmes' solution. Super cool using the array as data store. 
# kinda breaks my brain. I couldn't do this from scratch
# but I will come back and do the depth first + dp solution
input = sorted([0] + [int(e) for e in joltages])
print(input)
print('-----------------------------------------')
input += [max(input)+3]
print(input)
print('-----------------------------------------')
paths = [0] * (max(input)+1)
paths[0] = 1
print(paths)
print('-----------------------------------------')
for i in input:
    for j in (1,2,3):
        if i-j in input:
            paths[i] += paths[i-j]
            print(paths)
            print('-----------------------------------------')

print(paths)
print('-----------------------------------------')
print(paths[-1])

exit(0)

joltages.sort()
for x in range(len(joltages)-1):
    differences.append(joltages[x+1]-joltages[x])
differences.append(3)


def countOccurances(list):
    dict = {}
    for x in list:
        try:
            dict[x] += 1
        except:
            dict[x] = 1
    return dict


countDifferences = countOccurances(differences)
#print(f"Answer:{countDifferences[1]*countDifferences[3]}")
print(differences)







# # This was not an effective solution strategy
# def getTotalCombos(seet,num):
#     sum = 1
#     # seet = num
#     for sample in range(num,0,-1):
#         # print(sample)
#         sum += math.factorial(seet) / ((math.factorial(sample))* math.factorial(seet-sample))
#         # seet! / ( (sample!)*(seet-sample)!)
#     return sum



# sequentials = []
# differcount = 0
# while differcount < len(differences):
#     count = 0
#     while differences[differcount] == 1:
#         count += 1
#         differcount+=1
#     differcount += 1
#     sequentials.append(count)

# #print(sequentials)
# sum = 1
# imp_sequentials = []
# for x in sequentials:
#     y = x -1
#     if y > 0:
#         imp_sequentials.append(y)
# print(imp_sequentials)
# for imp in imp_sequentials:
#     sum += getTotalCombos(6,imp)
# print(sum)
# newsum = 0

# # 32768-19208 = 13560
# # Find number of elements that can be removed
# #   [1, 3,  1, 1, 1, 3,  1,  1,  3,  1,  3, 3]
# # (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)

# # (0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22) -- 11
# # (0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22) -- 6
# # (0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22) -- 6, 11
# # (0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22) 5, 
# # (0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22) -- 5, 11, 
# # (0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22) --5, 6
# # (0), 1, 4, 7, 10, 12, 15, 16, 19, (22) -- 5, 6, 11, 

# # 5
# # 6
# # 11
# # 5,11
# # 6,11
# # 5,6
# # 5,6,11

# # How to find total number: 
# # Find all numbers that can be removed. Count them. Create a combination
# # calculator and sum the result of every sample size from 1 to the total number
# # For the example above comb(set=3,sample=1) + comb(set=3,sample=2) + comb(set=3,sample=3) + 1 == 8
# #                                  3         +            3         +            1         + 1 == 8
# # that can be removed and then add 1 (for the original full set)

# # combinations formula:
# # set! / ( (sample!)*(set-sample)!)