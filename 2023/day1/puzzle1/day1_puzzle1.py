import sys, re
nums = []
with open(sys.argv[1]) as file:
    nums = file.readlines()
sum = 0
for x in nums:
    x = re.sub(r'[a-zA-Z\n]', '', x)
    num = ''
    if len(x) == 1:
        num = x + x
    else:
        num = x[0] + x[len(x) - 1]
    sum += int(num)
print(sum)