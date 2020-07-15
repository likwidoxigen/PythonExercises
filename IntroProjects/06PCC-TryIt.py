# 6-1: Person
# Use a dictionary to store information about a person you know. Store their first
#  name, last name, age, and the city in which they live. You should have keys suc
# h as first_name, last_name, age, and city. Print each piece of information store
# d in your dictionary.

person = {
    'first_name': 'John',
    'last_name': 'Smith',
    'age': 44,
    'city': 'Sao Paulo'
}

print(person)
print(
    f"{person['last_name']}, {person['first_name']} from {person['city']} age: {person['age']}"
)

# 6-2: Favorite Numbers
# Use a dictionary to store people’s favorite numbers. Think of five names, and us
# e them as keys in your dictionary. Think of a favorite number for each person, a
# nd store each as a value in your dictionary. Print each person’s name and their
# favorite number. For even more fun, poll a few friends and get some actual data
# for your program.


def favnum(s, n):
    print(f"{s}'s favorite number is {n}.")


fav_nums = {'steve': 5, 'tina': 11, 'hugh': 105, 'greg': 333, 'jason': 2}

num = fav_nums['hugh']
favnum("Hugh", num)

#6-3,4
# 6-5: Rivers
# Make a dictionary containing three major rivers and the country each river runs
# through. One key-value pair might be 'nile': 'egypt'.
#     Use a loop to print a sentence about each river, such as The Nile runs throu
# gh Egypt.
#     Use a loop to print the name of each river included in the dictionary.
#     Use a loop to print the name of each country included in the dictionary.
rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'yangtze': 'china',
}

for river, country in rivers.items():
    print(f"The river {river.title()} runs through {country.title()}")

for river in rivers.keys():
    print(f"I know about the river {river.title()}.")

for country in rivers.values():
    print(f"I know about a river in {country.title()}")

# 6-6: Polling
# Use the code in favorite_languages.py (page 104).
#     Make a list of people who should take the favorite languages poll. Include s
# ome names that are already in the dictionary and some that are not.
#     Loop through the list of people who should take the poll. If they have alrea
# dy taken the poll, print a message thanking them for responding. If they have no
# t yet taken the poll, print a message inviting them to take the poll.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']

for p, l in favorite_languages.items():
    print(f"{p.title()}'s most favorite language is {l.title()}")

for c in coders:
    if c in favorite_languages.keys():
        print(f"Thank you {c.title()} for taking the quiz!")
    else:
        print(f"{c.title()} please take the quiz!")


# 6-7: People
# Start with the program you wrote for Exercise 6-1 (page 102). Make two new dicti
# onaries representing different people, and store all three dictionaries in a lis
# t called people. Loop through your list of people. As you loop through the list,
#  print everything you know about each person.
def printPerson(p):
    print(
        f"{p['last_name']}, {p['first_name']} from {p['city']} age: {p['age']}"
    )


people = []

person1 = {
    'first_name': 'John',
    'last_name': 'Smith',
    'age': 44,
    'city': 'Sao Paulo'
}
person2 = {
    'first_name': 'Brian',
    'last_name': 'Winston',
    'age': 14,
    'city': 'Sherbrooke'
}
person3 = {
    'first_name': 'Kyle',
    'last_name': 'Smith',
    'age': 94,
    'city': 'Tampa'
}

people.append(person1)
people.append(person2)
people.append(person3)

for p in people:
    printPerson(p)

#6-8,9,10,11 Skipped