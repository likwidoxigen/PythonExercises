# 5-3: Alien Colors #1
# Imagine an alien was just shot down in a game. Create a variable called
# alien_color and assign it a value of 'green', 'yellow', or 'red'.
#     Write an if statement to test whether the alien’s color is green. If it is,
# print a message that the player just earned 5 points.
#     Write one version of this program that passes the if test and another that fa
# ils. (The version that fails will have no output.)

alien_color = 'green'
alien_color2 = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points!")

if alien_color2 == 'green':
    print("You just earned 5 points!")

# 5-4: Alien Colors #2
# Choose a color for an alien as you did in Exercise 5-3, and write an if-else cha
# in.
#     If the alien’s color is green, print a statement that the player just earned
#  5 points for shooting the alien.
#     If the alien’s color isn’t green, print a statement that the player just earn
# ed 10 points.
#     Write one version of this program that runs the if block and another that ru
# ns the else block.

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

if alien_color2 == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

#skipped 5-5

# 5-6: Stages of Life
# Write an if-elif-else cahin that determines a person’s stage of life. Set a valu
# e for the variable age, and then:
#     If the person is less than 2 years old, print a message that the person is a
#  baby.
#     If the person is at least 2 years old but less than 4, print a message that
# the person is a toddler.
#     If the person is at least 4 years old but less than 13, print a message that
#  the person is a kid.
#     If the person is at least 13 years old but less than 20, print a message that
#  the person is a teenager.
#     If the person is at least 20 years old but less than 65, print a message that
#  the person is a adult.
#     If the person is age 65 or older, print a message that the person is an elder.

age = 19
if age < 2:
    print("Baby")
elif age < 4:
    print("Toddler")
elif age < 13:
    print("Kid")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Elder")

# 5-7: Favorite Fruit
# Make a list of your favorite fruits, and then write a series of independent if s
# tatements that check for certain fruits in your list.
#     Make a list of your three favorite fruits and call it favorite_fruits.
#     Write five if statements. Each should check whether a certain kind of fruit
# is in your list. If the fruit is in your list, the if block should print a state
# ment, such as You really like bananas!


def youlike(s):
    print(f"You really like {s}!")


favorite_fruits = ["Pineapple", "Dragonfruit", "Avocado"]
#My solution didn't match theirs
for fruit in favorite_fruits:
    if fruit == 'Pineapple':
        youlike(fruit)
    if fruit == 'Tomato':
        youlike(fruit)
    if fruit == 'Cherry':
        youlike(fruit)
    if fruit == "Dragonfruit":
        youlike(fruit)
    if fruit == "Avocado":
        youlike(fruit)

#they used this syntax:
if 'Avocado' in fruit:
    youlike(fruit)

#5-8,9,10 Skipped
# 5-11: Ordinal Numbers
# Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordi
# nal numbers end in th, except 1, 2, and 3.
#     Store the numbers 1 through 9 in a list.
#     Loop through the list.
#     Use an if-elif-else chain inside the loop to print the proper ordinal ending
#  for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th",
#  and each result should be on a separate line.

ords = list(range(1, 10))
for o in ords:
    if o == 1:
        print(f"{o}st")
    elif o == 2:
        print(f"{o}nd")
    elif o == 3:
        print(f"{o}rd")
    else:
        print(f"{o}th")