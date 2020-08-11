with open("IntroProjects/PCCLearning_Python.txt") as file_object:
    contents = file_object.read()
    print(contents)

with open("IntroProjects/PCCLearning_Python.txt") as file_object:
    for line in file_object:
        print(line.rstrip().title())

with open("IntroProjects/PCCLearning_Python.txt") as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip().replace("python","java"))