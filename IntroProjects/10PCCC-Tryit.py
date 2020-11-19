with open("IntroProjects/PCCLearning_Python.txt") as file_object:
    """ Print file object as one lump """
    contents = file_object.read()
    print(contents)

with open("IntroProjects/PCCLearning_Python.txt") as file_object:
    """print file line by line"""
    for line in file_object:
        print(line.rstrip().title())

with open("IntroProjects/PCCLearning_Python.txt") as file_object:
    """create list of lines in the file"""
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip().replace("python","java"))


# name = input("What is your name? ")
# with open("IntroProjects/guest_book.txt", 'a') as file_object:
#     file_object.write(f'{name}\n')


try:
    print(5/0)
except ZeroDivisionError:
    print("We made a boo boo")

