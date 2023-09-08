Watermelon = [[0,1,1,0,0,1,0,1],[1,0,1,0,1,1,1,0],[0,1,0,0,1,0,0,0],[1,1,0,1,0,1,1,1],
[1,0,1,0,1,1,0,0],[0,0,1,0,1,1,0,0],[1,1,1,0,0,1,1,0],[0,0,0,0,0,1,1,0]]
def watermeloncalc(array):
    seeds1 = 0
    seeds2 = 0
    seeds3 = 0
    seeds4 = 0
    totalseeds = 0
    print(array)
    print("seeds = " + str(totalseeds))
    print("totalseeds = " + str(totalseeds))
    for row in range(len(array)-4):
        for col in range(len(array)-4):
            seeds1 = seeds1 + array[row][col]
            array[row][col] = "x"
    print(array)
    for row in range(len(array)-4):
        for col in range(len(array)-4):
            array[row][col] = 0
    if seeds1 > 5:
        totalseeds = seeds1
        print("seeds = " + str(seeds1))
        print("totalseeds = " + str(totalseeds))
    if seeds1 <= 5:
        seeds1 = 0
        print("seeds = " + str(seeds1))
        print("totalseeds = " + str(totalseeds))
    for col in range(len(array)):
        for row in range(len(array)-4):
            seeds2 = seeds2 + array[row][col]
            array[row][col] = "x"
    print(array)
    for col in range(len(array)):
        for row in range(len(array)-4):
            array[row][col] = 0
    if seeds2 > 5:
        print("seeds = " + str(seeds2))
        totalseeds = seeds1 + seeds2
        print("seeds = " + str(totalseeds))
    if seeds2 <= 5:
        seeds2 = 0
        print("seeds = " + str(seeds2))
        totalseeds = seeds1 + seeds2
        print("totalseeds = " + str(totalseeds))
    for row in range(len(array)-4):
        for col in range(len(array)):
            seeds3 = seeds3 + array[col][row]
            array[col][row] = "x"
    print(array)
    for row in range(len(array)-4):
        for col in range(len(array)):
            array[col][row] = 0
    if seeds3 > 5:
        print("seeds = " + str(seeds3))
        totalseeds = seeds1 + seeds2 + seeds3
        print("seeds = " + str(totalseeds))
    if seeds3 <= 5:
        seeds3 = 0
        print("seeds = " + str(seeds3))
        totalseeds = seeds1 + seeds2 + seeds3
        print("totalseeds = " + str(totalseeds))
    for col in range(len(array)):
        for row in range(len(array)):
            seeds4 = seeds4 + array[row][col]
            array[row][col] = "x"
    print(array)
    for col in range(len(array)):
        for row in range(len(array)):
            array[row][col] = 0
    if seeds4 > 5:
        print("seeds = " + str(seeds4))
        totalseeds = seeds1 + seeds2 + seeds3 + seeds4
        print("seeds = " + str(totalseeds))
    if seeds4 <= 5:
        print("seeds = " + str(seeds4))
        seeds4 = 0
        totalseeds = seeds1 + seeds2 + seeds3 + seeds4
        print("totalseeds = " + str(totalseeds))
watermeloncalc(Watermelon)


