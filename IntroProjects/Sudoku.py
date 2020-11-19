for repeatX in range (3):
    for repeatY in range(3):
        print("-------------------------")
        xStart = 0 + 3*repeatX
        xEnd = 3 + 3*repeatX
        yStart = 0 + 3*repeatY
        yEnd = 3 +3*repeatY
        for x in range(xStart,xEnd,1):
            coords = []
            for y in range(yStart,yEnd,1):
                coords.append(f"{x},{y}")
            print(coords)