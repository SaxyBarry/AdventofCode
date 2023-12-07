import sys, re, math

def convert(map, source):
    dest = 0
    for x in map:
        sourceStart = int(x[1])
        rangeLen = int(x[2])
        destStart = int(x[0])
        if source >= sourceStart and source <= sourceStart+rangeLen:
            dest = destStart + (source - sourceStart)
            break
    if dest == 0:
        dest = source
    return dest

with open(sys.argv[1]) as file:
    lines = file.read()
    lines = lines.strip()
    # Cleaning and separating the data
    # sources will be the starting and will fit in the ranges in the maps below
    seeds = re.findall("(?<=seeds:) [0-9 ]*", lines)[0].strip().split()
    # Now data is separated into sets of 3 within each of these maps with the following 
    # Index 0 = Starting Range
    # Index 1 = Destination Range
    # Index 2 = Numbers in Range
    seedToSoil = [x.split() for x in re.findall("(?<=seed-to-soil map:)[0-9 \n]*", lines)[0].strip().split("\n")]
    soilToFert = [x.split() for x in re.findall("(?<=soil-to-fertilizer map:)[0-9 \n]*", lines)[0].strip().split("\n")]
    fertToWater = [x.split() for x in re.findall("(?<=fertilizer-to-water map:)[0-9 \n]*", lines)[0].strip().split("\n")]
    waterToLight = [x.split() for x in re.findall("(?<=water-to-light map:)[0-9 \n]*", lines)[0].strip().split("\n")]
    lightToTemp = [x.split() for x in re.findall("(?<=light-to-temperature map:)[0-9 \n]*", lines)[0].strip().split("\n")]
    tempToHumid = [x.split() for x in re.findall("(?<=temperature-to-humidity map:)[0-9 \n]*", lines)[0].strip().split("\n")]
    humidToLocation = [x.split() for x in re.findall("(?<=humidity-to-location map:)[0-9 \n]*", lines)[0].strip().split("\n")]
    locations = []
    for seed in seeds:
        seed = int(seed)
        soil = convert(seedToSoil, seed)
        fert = convert(soilToFert, soil)
        water = convert(fertToWater, fert)
        light = convert(waterToLight, water)
        temp = convert(lightToTemp, light)
        humid = convert(tempToHumid, temp)
        location = convert(humidToLocation, humid)
        locations.append(location)
    locations.sort(reverse=False)
    print(locations[0])

        