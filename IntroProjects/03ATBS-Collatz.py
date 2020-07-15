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