from PCCCprinting_functions import make_car, print_models as cars_go_vroom


def display_message():
    print("We are learning about functions!")


display_message()


def favorite_book(title):
    print(f"One of my favorite books is {title.title()}")


favorite_book("Kiln People")


def make_album(name, title, numSongs=None):
    album = {'Artist_Name': name, 'Album_Title': title}
    if numSongs:
        album["Song_Count"] = numSongs
    return album


albums = []
albums.append(make_album('Marylin Manson', 'Mechanical Animals'))
albums.append(make_album('Less Than Jake', 'Borders and Boundaries', 10))
albums.append(make_album("N'Sync", 'No Strings Attached'))
print(albums)

#Start with your program from Exercise 8-7. Write a while loop that allows users
#to enter an album’s artist and title. Once you have that information, call
#make_album() with the user’s input and print the dictionary that’s created. Be
#sure to include a quit value in the while loop.

# albumInput = []
# albums2 = []
# artist = ""
# while (artist != "QUIT"):
#     artist = input("(Type QUIT to exit)Input the artist: ")
#     if (artist == "QUIT"):
#         break
#     title = input("Input the album name: ")
#     albumInput.append({'Artist_Name': artist, 'Album_Title': title})

# for al in albumInput:
#     albums2.append(make_album(al['Artist_Name'], al['Album_Title']))

# print(albums2)


# 8-9. Messages: Make a list containing a series of short text messages. Pass
# the list to a function called show_messages(), which prints each text message.
def printMessages(msgs):
    x = 1
    for msg in msgs:
        print(f'1: {msg} ')
        x += 1


messages = [
    "Hello", "I am a message", "Messages are great", "Thank you for watching"
]

# printMessages(messages)

# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.
sentMessages = []


def sendMessages(msgs):
    while msgs:
        msg = msgs.pop()
        print(f'Sending: {msg}')
        sentMessages.append(msg)


# sendMessages(messages)

# print("Messages in Queue")
# printMessages(messages)
# print("Sent messages")
# printMessages(sentMessages)

# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
# function send_messages() with a copy of the list of messages. After calling
# the function, print both of your lists to show that the original list has
# retained its messages.

sendMessages(messages[:])

print("Messages in Queue")
printMessages(messages)
print("Sent messages")
printMessages(sentMessages)

# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the
# sandwich that’s being ordered. Call the function three times, using a
# different number of arguments each time.


def sandwichContents(*stuff):
    print("You will have the following stuff on your sandwich!")
    print(stuff)


sandwichContents('Salami', 'Capicola', 'Pepperoni')
sandwichContents('Meatball', 'Marinara', 'Roasted Red Peppers')
sandwichContents('Honey Roasted Chicken', 'Pepperioni', 'Lettuce', 'Oregano',
                 'Oil', 'Vinegar')

# 8-13. User Profile: Start with a copy of user_profile.py from page 149. Build
# a profile of yourself by calling build_profile(), using your first and last
# names and three other key-value pairs that describe you.


def buildProfile(first_name, last_name, **userInfo):
    userInfo['first_name'] = first_name
    userInfo['last_name'] = last_name
    return userInfo


userProfile = buildProfile('Road',
                           'Runner',
                           speed='Very Fast',
                           nemesis='Wile E. Coyote')

print(userProfile)

# 8-14. Cars: Write a function that stores information about a car in a
# dictionary. The function should always receive a manufacturer and a model
# name. It should then accept an arbitrary number of keyword arguments. Call the
# function with the required information and two other name-value pairs, such as
# a color or an optional feature. Your function should work for a call like this
# one:

# car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Print the dictionary that’s returned to make sure all the information was
# stored correctly.

# def make_car(make, model, **carInfo):
#     carInfo['make'] = make
#     carInfo['model'] = model
#     return carInfo

mahCar = make_car('Toyota', '4 Runner', speed='Ok', color='Purple')

print(mahCar)

# 8-15. Printing Models: Put the functions for the example printing_models.py in
# a separate file called printing_functions.py. Write an import statement at the
# top of printing_models.py, and modify the file to use the imported functions.

cars_go_vroom(mahCar)

# 8-16. Imports: Using a program you wrote that has one function in it, store
# that function in a separate file. Import the function into your main program
# file, and call the function using each of these approaches:

# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

# 8-17. Styling Functions: Choose any three programs you wrote for this chapter,
# and make sure they follow the styling guidelines described in this section.

# obj.attribute is good dictionaries aren't like that. use ['attr']