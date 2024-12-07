#!/bin/python3
def get_data() -> list:
    """
        Return: List of each lines reads from inputs
    """
    # with open("little_dummy.txt", "r") as f:
    # with open("dummy.txt", "r") as f:
    with open("data.txt", "r") as f:
        return [line[:-1] for line in f]

PART_ONE = False
res = 0
data = get_data()
###############################################################################
line_to_split = -200
# line_to_split = -6

rules = data[:line_to_split - 1]
ordering = data[line_to_split:]
preceed = {}
print(rules[:-5])
for rule in rules:
    right, left = rule.split('|')
    if int(left) not in preceed:
        preceed[int(left)] = set()
    preceed[int(left)].add(int(right))

for elem in ordering:
    int_elem = list(map(int, elem.split(',')))
    res_ok = True

    # Compute all possible orders
    i = 0 
    while i < len(int_elem):
        # if no rules about preceeding value, continue
        if int_elem[i] not in preceed:
            i += 1
            continue
        # Otherwise verify that no next one preceed him
        nexts = int_elem[i + 1:]
        for j, n in enumerate(nexts):
            if n not in preceed[int_elem[i]]:
                continue
            res_ok = False
            if PART_ONE:
                i += 1
                break
            # making swap on int_elem with i j
            int_elem[i], int_elem[j + i + 1] = int_elem[j + i + 1], int_elem[i]
            break
        else:
            i += 1
    if res_ok == PART_ONE:
        print(int_elem)
        res += int_elem[len(int_elem) // 2]


###############################################################################
print(res)
