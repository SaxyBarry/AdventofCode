import sys, re
redLimit = 12
blueLimit = 14
greenLimit = 13
sumID = 0
with open(sys.argv[1]) as file:
    lines = file.readlines()
    id = 1
    for x in lines:
        # Evil looking one-liners here. Essentially just extracting out the reds, blues and greens from each line, 
        # then stripping all characters and converting the counts to ints and finally finiding the max of those counts for comparison later
        largestRed = max(list(map(lambda y: int(re.sub("[a-zA-Z]", '', y)), re.findall("([0-9]+ red)+", x))))
        largestBlue = max(list(map(lambda y: int(re.sub("[a-zA-Z]", '', y)), re.findall("([0-9]+ blue)+", x))))
        largestGreen = max(list(map(lambda y: int(re.sub("[a-zA-Z]", '', y)), re.findall("([0-9]+ green)+", x))))
        if largestGreen <= greenLimit and largestBlue <= blueLimit and largestRed <= redLimit:
            sumID += id
        id+=1
print(sumID)
