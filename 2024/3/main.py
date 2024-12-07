#!/bin/python3
def get_data() -> list:
    """
        Return: List of each lines reads from inputs
    """
    # with open("dummy.txt", "r") as f:
    with open("data.txt", "r") as f:
        return [line[:-1] for line in f]
data = get_data()


import re
res = 0
regex = r'mul\([0-9]?[0-9]?[0-9],[0-9]?[0-9]?[0-9]\)'
line = "".join(data) + "do()"
print(len(line) + len(data))
newline = re.sub(r"don't\(\).*?do\(\)", "", line) 
for elem in re.findall(regex, newline):
    ints = elem.split(',')
    res += int(ints[0][4:]) * int(ints[1][:-1])
print(res)

