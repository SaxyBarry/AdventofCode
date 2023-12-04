import sys, re, math
# What cards need processed, will be added to
queue = [] 
# What are the original cards, will not be modified
cardDict = {}
valueDict = {}
with open(sys.argv[1]) as file:
    lines = file.readlines()
    # Mark all the cards that exist, and add them to the queue
    count = 0
    for x in lines:
        cardDict[count] = x
        queue.append(count)
        count += 1
    cardIndex = 0
    for x in queue:
        cardIndex = x+1
        count = 0
        # Finding all the matches in the given card
        # (?<=:)(.*?)(?=\|) Everything between : and |
        # (?<=\|)(.*) Everything after |
        winningNums = re.findall("(?<=:)(.*?)(?=\|)", cardDict[x])[0].strip().split()
        myNums = re.findall("(?<=\|)(.*)", cardDict[x])[0].strip().split()
        count = len(set(winningNums) & set(myNums))
        # Add possible cards to the queue
        result2 = list(cardDict.keys())[cardIndex:len(list(cardDict.keys()))]
        if(len(result2) != 0):
            for i in range(count):
                index = i % len(result2)
                queue.append(result2[index])

    print(len(queue))