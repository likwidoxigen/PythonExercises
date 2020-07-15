#Automate the Boring Stuff Collatz sequence
# The Collatz Sequence

# Write a function named collatz() that has one parameter named number. If number
# is even, then collatz() should print number // 2 and return this value. If
# number is odd, then collatz() should print and return 3 * number + 1.

# Then write a program that lets the user type in an integer and that keeps
# calling collatz() on that number until the function returns the value 1.
# (Amazingly enough, this sequence actually works for any integer—sooner or
# later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure
# why. Your program is exploring what’s called the Collatz sequence, sometimes
# called “the simplest impossible math problem.”)

# Remember to convert the return value from input() to an integer with the int()
# function; otherwise, it will be a string value.

# Hint: An integer number is even if number % 2 == 0, and it’s odd if number % 2
# == 1.
import time, sys


def collatz(n):
    if (n % 2 == 0):
        return int(n / 2)
    else:
        return 3 * n + 1


number = int(input("Please input a number: "))
while (number != 1):
    number = collatz(number)
    print(number)
    time.sleep(0.01)