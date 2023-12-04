import sys, re
sumNums = 0
with open(sys.argv[1]) as file:
    lines = file.readlines()
    symbolPositions = []
    numPositions = []
    array = []
    y_axis = 0
    # Creating a 2-D array representation of the text input
    for x in lines:
        line = []
        x_axis = 0
        for y in x:
            line.append(y)
            # Finding the positions of all the * symbols
            if y == '*':
                symbolPositions.append((x_axis, y_axis))
            # Finding index of numbers
            if y.isdigit():
                numPositions.append((x_axis, y_axis))
            x_axis +=1
        array.append(line)
        y_axis+=1
    # Finding numbers that are adjacent to *s, creating a dict to keep track of the numbers each * is adjacent to
    validNumberPositionsandSymbols = {}
    validNumberPositions = []
    for x in numPositions:
        for y in symbolPositions:
            if -1 <= x[1] - y[1] <= 1 and -1 <= x[0] - y[0] <= 1 :
                if y in validNumberPositionsandSymbols.keys():
                    validNumberPositionsandSymbols[y].append(x)
                else:
                    validNumberPositionsandSymbols[y] = [x]
                validNumberPositions.append(x)
    # Grouping together all numbers
    numbers = []
    index = 0
    while index < len(numPositions):
        number = [numPositions[index]]
        x = numPositions[index]
        streak = True
        leng = 1
        while streak:
            if (x[0]+leng, x[1]) in numPositions:
                number.append((x[0]+leng,x[1]))
                leng+=1
            else:
                streak = False
        index += leng
        numbers.append(number)
    # Finding all valid numbers
    # More specifically: Finding complete valid numbers, not just valid digits 
    validNumbers = []
    for x in validNumberPositions:
        for y in numbers:
            if x in y and not y in validNumbers:
                validNumbers.append(y)
    # Replace the digits in the gears dict with the numbers, removing duplicates
    gears = {}
    for x in validNumbers:
        for y in validNumberPositionsandSymbols.keys():
            for z in validNumberPositionsandSymbols[y]:
                if z in x:
                    if y in gears.keys() and not x in gears[y]:
                        gears[y].append(x)
                    elif not y in gears.keys():
                        gears[y] = [x]
    # Finding the gear ratio and sum of the valid gears
    sum = 0
    for x in gears.keys():
        product = 0
        if len(gears[x]) == 2:
            product = 1
            for y in gears[x]:
                number = ""
                for z in y:
                    number += array[z[1]][z[0]]
                product *= int(number)
        sum+=product
    print(sum)


