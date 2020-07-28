# 7-1: Rental Car
# Write a program that asks the user what kind of rental car they would like. Prin
# t a message about that car, such as “Let me see if I can find you a Subaru”.
# car = input('What kind of car would you like: ')
# print(f"Sounds great. Lets get you a {car}!")

# 7-2: Restaurant Seating
# Write a program that asks the user how many people are in their dinner group. If
#  the answer is more than eight, print a message saying they’ll have to wait for
# a table. Otherwise, report that their table is ready.

# # groupSize = input('How many are in your party? ')
# if int(groupSize) < 8:
#     print("Your table is ready.")
# else:
#     print("Ya'll will need to wait for a table.")

# # num = input("Please input an number: ")

# if int(num) % 10 == 0:
#     print("That number was divisible by 10!")
# else:
#     print("That number was not divisible by 10!")

# 7-8: Deli
# Make a list called sandwich_orders and fill it with the names of various sandwic
# hes. Then make an empty list called finished_sandwiches. Loop through the list o
# f sandwich orders and print a message for each order, such as I made your tuna s
# andwich. As each sandwich is made, move it to the list of finished sandwiches. A
# fter all the sandwiches have been made, print a message listing each sandwich th
# at was made.

sandwich_orders = ['salami', 'italian', 'meatball', 'reuben', 'clam']
finished_sandwiches = []

#remove all pastrami orders
while 'pastrami' in sandwich_orders:
    print("We are out of pastrami")

while sandwich_orders:
    currentSandwich = sandwich_orders.pop()
    print(f"I am now making your {currentSandwich} sandwich.")
    finished_sandwiches.append(currentSandwich)

print("I have made the following sandwiches:")
for sand in finished_sandwiches:
    print(sand.title())

# 7-10: Dream Vacation
# Write a program that polls users about their dream vacation. Write a prompt simi
# lar to If you could visit one place in the world, where would you go? Include a
# block of code that prints the results of the poll.

dreamVacations = []
cont = 'yes'
while cont.lower() == 'yes':
    dreamVacation = {}
    name = input("What is your name? ")
    location = input(
        "If you could travel anywhere in the world where would it be? ")
    dreamVacation['name'] = name
    dreamVacation['location'] = location
    dreamVacations.append(dreamVacation)
    cont = input('Would you like to continue? ')

print("The results of the poll are: ")
for dv in dreamVacations:
    print(f"{dv['name'].title()} would like to go to {dv['location']}")
