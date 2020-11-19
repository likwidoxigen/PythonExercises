def readInt(prompt) :
    valid = False
    while not valid :
        try :
            x = int(input(prompt))
            valid = True
        except ValueError as e:
            print ('Not an integer number. Try Again.')
    return x

def readFloat(prompt) :
    valid = False
    while not valid :
        try :
            x = float(input(prompt))
            valid = True
        except ValueError as e:
            print ('Not an float number. Try Again.')
    return x

a = readInt("Gimme integer:")
print(a)

b = readFloat("Gimme float:")
print(b)