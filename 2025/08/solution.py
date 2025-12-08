
# --- Constants ---#
INPUT_SHORT_PATH = "input_short.txt"
INPUT_PATH = "input.txt"
STREAM = ""

# --- Read content of input ---#
with open(INPUT_PATH, "r") as inpf:
    STREAM = inpf.read().split("\n")

# --- Main solution ---#

def euclidian_dist_3D(x, y):
    return ((x[0] - y[0])**2 + abs(x[1] - y[1])**2 + abs(x[2] - y[2])**2) ** 0.5

# Save N first distances
# N = 10 # short input
N = 1000 # normal input

distances = [float('inf')] * N
idx_shortest_dist = [None] * N

from bisect import insort

# Convert each line as 3D array point
STREAM = list(map(lambda x: list(map(int, x.split(','))), STREAM))

for i in range(len(STREAM)):
    for j in range(i + 1, len(STREAM)):
        c_dist = euclidian_dist_3D(STREAM[i], STREAM[j])

        # If we are lower than the bigger distance, insort
        if c_dist < distances[-1]:
            insort(distances, c_dist)
            distances.pop(-1)

            distance_idx = distances.index(c_dist)
            idx_shortest_dist = idx_shortest_dist[:distance_idx] + [[i, j]] + idx_shortest_dist[distance_idx:]

            idx_shortest_dist.pop(-1)
# Now that we have our 1000 shortest path, plug circuits
# At the beggining they are all plugged to them self
plugged = {
    idx: [idx]
    for idx in range(len(STREAM))
}
print("parsing final answer")

while len(idx_shortest_dist) > 0:
    
    # Get the next element in the list
    path = idx_shortest_dist.pop(0)

    # if they are already plugged together continue
    if path[0] == path[1]:
        continue

    # plugged cable together
    plugged[path[0]].extend(plugged[path[1]])
    del plugged[path[1]]

    # replace the second plug by the base
    for i in range(len(idx_shortest_dist)):
        if idx_shortest_dist[i][0] == path[1]:
            idx_shortest_dist[i][0] = path[0]
        if idx_shortest_dist[i][1] == path[1]:
            idx_shortest_dist[i][1] =path[0]

biggest_sol = [-1] * 3
# Compute the final solution
for elem in plugged.values():
    insort(biggest_sol, len(elem))
    biggest_sol.pop(0)

print(biggest_sol[0] * biggest_sol[1] * biggest_sol[2])