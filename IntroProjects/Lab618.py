''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
#d = int(input())
#e = int(input())
#f = int(input())

found = False
for x in range(-10, 11):
    j = x*a
    for y in range(-10,11):
        k = y*b
        if j + k == c:
            print('x =', x, ', ' 'y =', y)
            found = True
            ansX = x
            ansY = y

if found == False:
    print("There is no solution")