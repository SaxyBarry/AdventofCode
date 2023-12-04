import sys, re, math
sum = 0
with open(sys.argv[1]) as file:
    lines = file.readlines()
    # (?<=:)(.*?)(?=\|) Everything between : and |
    # (?<=\|)(.*) Everything after | 
    for x in lines:
        count = 0
        winningNums = re.findall("(?<=:)(.*?)(?=\|)", x)[0].strip().split()
        myNums = re.findall("(?<=\|)(.*)", x)[0].strip().split()
        count = len(set(winningNums) & set(myNums))
        if count > 0:
            sum += 2**(count - 1)
    print(sum)

        