#Automate the Boring Stuff Chapter 2 Work

a = 1
b = 2

print(a)
print(b)
a, b = b, a

print(a)
print(b)

name = "Bryce"
password = "aPizzA"

if (name == "Bryce"):
    print("HI " + name)
    if (password == "PizzA"):
        print("User Authorized")
    elif (password == "aPizzA"):
        print("I'm Hungry too")
    else:
        print("Authorization Failed")
else:
    print("User bad")

yearToCheck = int(input("What Year would you like to check? "))
checkText = "is not"
if (yearToCheck % 4 == 0 and yearToCheck % 100 != 0 or yearToCheck % 400 == 0):
    checkText = "is"
    print('here')

print(f"The year {yearToCheck} {checkText} a leap year!")
