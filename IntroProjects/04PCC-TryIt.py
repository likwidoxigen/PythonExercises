#Python Crash course
# 4-3: Counting to Twenty
# Use a for loop to print the numbers from 1 to 20, inclusive.

for num in range(1, 21):
    print(num)

# 4-5: Summing a Million
# Make a list of the numbers from one to one million, and then use min() and max()
#  to make sure your list actually starts at one and ends at one million. Also, us
# e the sum() function to see how quickly Python can add a million numbers.

list = list(range(1, 1000001))
if max(list) == 1000000 and min(list) == 1:
    print("List goes from 1 to 1,000,000")
    print(f"{sum(list)} is the sum of the list!")
else:
    print("The list is not from 1 to 1,000,000")

# 4-7: Threes
# Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the
# numbers in your list.
list2 = []
for n in range(3, 31, 3):
    list2.append(n)
print(list2)

# 4-8: Cubes
# A number raised to the third power is called a cube. For example, the cube of 2
# is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cu
# be of each integer from 1 through 10), and use a for loop to print out the value
#  of each cube.

cubes = []
for n in range(1, 10):
    cubes.append(n**3)
print(cubes)

#4-8: Cubes
#Generate using list comprehension
cubes2 = [v**3 for v in range(1, 11)]
print(cubes)