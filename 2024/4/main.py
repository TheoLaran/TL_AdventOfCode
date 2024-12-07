#!/bin/python3
def get_data() -> list:
    """
        Return: List of each lines reads from inputs
    """
    # with open("little_dummy.txt", "r") as f:
    # with open("dummy.txt", "r") as f:
    with open("data.txt", "r") as f:
        return [line[:-1] for line in f]
data = get_data()


from collections import deque

def search_arround(char, data, point, data_dim):
    matches = []
    for i in range(max(0, point[0] - 1), min(data_dim[0] - 1, point[0] + 1)):
        for j in range(max(0, point[1] - 1), min(data_dim[1] + 1, point[1] + 1)):
            if data[i][j] == char:
                matches.append((i, j))
    return matches

sens = [
    (-1,-1),
    (1,1)
]

F = deque()

res = 0

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if data[i][j] != "A":
            continue
        if  i < 1 or i >= len(data) - 1 or j < 1 or j >= len(data[0]) - 1:
            continue
        nb_mas = 0
        if  data[i + 1][j + 1] == "M" and data[i - 1][j - 1] == "S":
                nb_mas += 1
        if  data[i + 1][j + 1] == "S" and data[i - 1][j - 1] == "M":
                nb_mas += 1
        if  data[i + 1][j - 1] == "M" and data[i - 1][j + 1] == "S":
                nb_mas += 1
        if  data[i + 1][j - 1] == "S" and data[i - 1][j + 1] == "M":
                nb_mas += 1
        
        res += 1 if (nb_mas == 2) else 0
print(res)
