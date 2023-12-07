import sys, re, math

def reverseConvert(map, source):
    dest = 0
    for x in map:
        sourceStart = int(x[0])
        rangeLen = int(x[2])
        destStart = int(x[1])
        if source >= sourceStart and source <= sourceStart+rangeLen:
            dest = destStart + (source - sourceStart)
            break
    if dest == 0:
        dest = source
    return dest

def generate_pairs(arr):
    pairs = []
    # Finding cooresponding start, length numbers
    for i in range(0, len(arr), 2):
        start_number = int(arr[i])
        range_count = int(arr[i + 1])
        pairs.append((start_number, start_number+range_count))
    return pairs
    

def processSeeds(pairs, lines):
    print("start")
    seedToSoil = [x.split() for x in re.findall("(?<=seed-to-soil map:)[0-9 \n]*", lines)[0].strip().split("\n")]
    soilToFert = [x.split() for x in re.findall("(?<=soil-to-fertilizer map:)[0-9 \n]*", lines)[0].strip().split("\n")]
    fertToWater = [x.split() for x in re.findall("(?<=fertilizer-to-water map:)[0-9 \n]*", lines)[0].strip().split("\n")]
    waterToLight = [x.split() for x in re.findall("(?<=water-to-light map:)[0-9 \n]*", lines)[0].strip().split("\n")]
    lightToTemp = [x.split() for x in re.findall("(?<=light-to-temperature map:)[0-9 \n]*", lines)[0].strip().split("\n")]
    tempToHumid = [x.split() for x in re.findall("(?<=temperature-to-humidity map:)[0-9 \n]*", lines)[0].strip().split("\n")]
    humidToLocation = [x.split() for x in re.findall("(?<=humidity-to-location map:)[0-9 \n]*", lines)[0].strip().split("\n")]
    pairs = sorted(pairs, key=lambda x: x[1])
    i = 0
    found = False
    while i < pairs[len(pairs)-1][1] and found == False:
        contains = False
        humid = reverseConvert(humidToLocation, i)
        temp = reverseConvert(tempToHumid, humid)
        light = reverseConvert(lightToTemp, temp)
        water = reverseConvert(waterToLight, light)
        fert = reverseConvert(fertToWater, water)
        soil = reverseConvert(soilToFert, fert)
        seed = reverseConvert(seedToSoil, soil)
        for x in pairs:
            if seed >= x[0] and seed <=x[1]:
                print(i)
                contains = True
        if contains == True:
            found = True
        i+=1

if __name__ == '__main__':    
    with open(sys.argv[1]) as file:
        lines = file.read()
        lines = lines.strip()
        seeds = re.findall("(?<=seeds:) [0-9 ]*", lines)[0].strip().split()
        seeds = generate_pairs(seeds)
        processSeeds(seeds, lines)

    


    

        