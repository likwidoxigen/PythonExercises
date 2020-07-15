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
