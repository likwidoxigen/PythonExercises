#Automate the boring stuff Zig Zag Stars
# Let’s use the programming concepts you’ve learned so far to create a small anima
# tion program. This program will create a back-and-forth, zigzag pattern until th
# e user stops it by pressing the Mu editor’s Stop button or by pressing CTRL-C. W
# hen you run this program, the output will look something like this:
#     ********
#    ********
#   ********
#  ********
# ********
#  ********
#   ********
#    ********
#     ********

import time, sys
spaces = 0
NUMSTARS = 8
indentIncreasing = True

try:
    while True:
        print(" " * spaces + "*" * NUMSTARS)
        if spaces >= 4:
            indentIncreasing = False
        elif spaces <= 1:
            indentIncreasing = True

        if indentIncreasing:
            spaces += 1
        else:
            spaces -= 1
        time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()
