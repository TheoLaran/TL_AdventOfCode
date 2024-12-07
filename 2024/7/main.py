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
PART_ONE = False
DEBUG = False
CONCAT = lambda x, y: int(str(x) + str(y))

def is_possible(target, list_elem):
    if DEBUG:
        print(target, list_elem)
        print((not PART_ONE) and (str(target) == (str(list_elem[1]) + str(list_elem[0]))))
    
    if len(list_elem) == 2:
        return (list_elem[0] * list_elem[1] == target ) or\
               (list_elem[0] + list_elem[1] == target ) or\
               (not PART_ONE) and (str(target) == (str(list_elem[1]) + str(list_elem[0])))

    if target % list_elem[0] == 0:
        if is_possible(target // list_elem[0], list_elem[1:]):
            return True
    
    if is_possible(target - list_elem[0], list_elem[1:]):
        return True

    if PART_ONE:
        return False

    # For part two try again by concatenating values

    if len(str(list_elem[0])) < len(str(target)) and str(list_elem[0]) == str(target)[-len(str(list_elem[0])):]:
        return is_possible(
                int(
                    str(target)[:-len(str(list_elem[0]))]
                ),
                list_elem[1:]
            )
        
    return False

for line in data:
    target, values = line.split(":")
    values = list(map(int, values.split()))[::-1]
    target = int(target)
    res += target if is_possible(target, values) else 0
    # DEBUG = False
###############################################################################
print(res)
