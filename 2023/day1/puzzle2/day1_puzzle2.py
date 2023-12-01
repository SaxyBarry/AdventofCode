import sys, re

# Takes in a string, replaces number-words and returns a string with only numbers
def fixString(s):
    # dict of numbers and their word matchings
    # added first and last numbers to each number to account for oneightwone == 1821
    words_to_numbers = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine': 'n9e'
    }
    # constructing the regex pattern to match number-words in the string
    # (one|two|three|four|five|six|seven|eight|nine)
    pattern = re.compile(r'(' + '|'.join(words_to_numbers.keys()) + r')')
    # Replacing all of the number-words matched with their number
    # Looping to account for oneightwone == 1821, but should most of the time only run 1 extra time
    while pattern.search(s):
        s = re.sub(pattern, lambda x: words_to_numbers[x.group()], s)
    # Returning the string without any letters, only numbers
    return re.sub(r'[a-zA-Z\n]', '', s)

nums = []
with open(sys.argv[1]) as file:
    nums = file.readlines()
sum = 0
count = 0
for x in nums:
    count +=1
    x = fixString(x)
    num = ''
    if len(x) == 1:
        num = x + x
    else:
        num = x[0] + x[len(x) - 1]
    sum += int(num)
print(sum)