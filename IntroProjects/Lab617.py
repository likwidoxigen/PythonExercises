lines = []
line = input()
while line not in ('Done', 'done', 'd'):
    lines.append(line)
    line = input()
for line in reversed(lines):
    print(line[::-1])
