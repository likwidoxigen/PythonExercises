lines = []
userInput = input()
while userInput not in ('Done', 'done', 'd'):
    lines.append(userInput)
    userInput = input()

for line in lines:
    print(line)
    
print (lines)
#while lines not in ('Done', 'done', 'd'):
#    for i in range(len(lines)):
#        i = (0-1-i)
#    print(lines[i], end='')
#    lines = input()


#for line in reversed(lines):
#    print(line, end= '')
    