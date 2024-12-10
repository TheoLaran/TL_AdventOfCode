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

def insert_in_string(string, value, index):
    if index == len(string):
        return string[:-1] + value
    return string[:index] + value + string[index + 1:]

###############################################################################
data = list(map(int, data[0]))
nbrs = data[::2]
dots = data[1::2] + [0]
str_res = []

# use double pointer to browse string
p1 = 0
###
p2 = len(nbrs) - 1
###
nb_char_left_end = int(nbrs[p2])

# Values
v1 = 0
###
v2 = len(nbrs) - 1

debug_str = ""
chck_sum_ptr = 0
# first create string with dots
for i, elems in enumerate(zip(nbrs, dots)):
    n, d = elems
    str_res += [str(i)] * n
    str_res += ["."] * d

# Then fill it
if PART_ONE:
    p1 = 0
    p2 = len(str_res) - 1
    while p1 < p2:
        if str_res[p1] == "." and str_res[p2] != ".":
            # Replace
            str_res[p1] = str_res[p2]
            str_res[p2] = "."

        if str_res[p1] != ".":
            p1 += 1

        if str_res[p2] == ".":    
            p2 -= 1
else:
    p2 = len(nbrs) - 1
    # Use P1 for dots and P2 for nbrs
    while p2 > 0:
        value = nbrs[p2]

        idx = next((
                    i for i in range(p2)\
                    if dots[i] >= value
                ),
                None
            )

        # If there is not dots behind it continue
        if idx is None:
            p2 -= 1
            continue

        # Convert dot id to data position
        dots_idx = sum(data[:idx*2 + 1])
        p2_idx = sum(data[:p2*2])

        # Replace
        str_res[dots_idx:dots_idx + value] = [p2] * value
        ###
        str_res[p2_idx: p2_idx + value] = ["."] * value
        
        # Decrease nb of dots
        dots[idx] -= value

        # Increase nb of numbers
        data[idx * 2] += value
        data[idx * 2 + 1] -= value
        p2 -= 1

p1 = 0
p2 = len(nbrs) - 1
# while True:
#     # Fill first value with numbers
#     for _ in range(nbrs[p1]):
#         debug_str += str(v1)
#         res += chck_sum_ptr * v1
#         chck_sum_ptr += 1

#     # Then manage dots
#     if PART_ONE:
#         for i in range(dots[p1]):
#             debug_str += str(v2)
#             res += v2 * chck_sum_ptr
#             chck_sum_ptr += 1
#             nb_char_left_end -= 1
#             if nb_char_left_end == 0:
#                 p2 -= 1
#                 v2 -= 1
#                 nb_char_left_end = nbrs[p2]
#     else:
#         # TODO: Find next v2 value that fit in
#         # TODO: Add it in string and fill with dot, increase chck sum each time
#         pass
#     v1 += 1
#     p1 += 1
#     # check if v1 == v2 then complete with remaining size
#     if v1 >= v2:
#         for _ in range(nb_char_left_end):
#             debug_str += str(v2)
#             res += v2 * chck_sum_ptr
#             chck_sum_ptr += 1
#         break
#     # At the end increment each values that are not in string, ie that does not fit
# print(debug_str[:100], str_res[:100], sep="\n")


"""
while True:
    # Create first
    str_res += [str(v1)] * int(nbrs[p1])
        
    for i in range(int(dots[p1])):
        str_res += [str(v2)]
        nb_char_left_end -= 1
        if nb_char_left_end == 0:
            p2 -= 1
            v2 -= 1
            nb_char_left_end = int(nbrs[p2])

    v1 += 1
    p1 += 1
    # check if v1 == v2 then complete with remaining size
    if v1 >= v2:
        str_res += str(v2) * nb_char_left_end
        break
"""
int_res = list(map(lambda x: int(x) if x != "." else 0, str_res))

import numpy as np
r = np.arange(0, len(int_res))
res = np.dot(r, int_res)
print(res)

###############################################################################

