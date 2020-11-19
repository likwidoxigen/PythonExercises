''' Read in first equation, ax + by = c '''
a1 = int(input())
b1 = int(input())
c1 = int(input())

''' Read in second equation, dx + ey = f '''
a2 = int(input())
b2 = int(input())
c2 = int(input())

solved = False
for x in range(-10, 11):
    for y in range(-10,11):
        if a1*x + b1*y == c1:
            if a2*x + b2*y == c2:
                print('x =', x, ', ' 'y =', y)
                solved = True

if solved == False:
    print("There is no solution.")