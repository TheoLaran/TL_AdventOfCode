
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
# N = 1000 # normal input

from bisect import insort

# Convert each line as 3D array point
STREAM = list(map(lambda x: list(map(int, x.split(','))), STREAM))

# Now that we have our 1000 shortest path, plug circuits
# At the beggining they are all plugged to them self
plugged = {
    idx: [idx]
    for idx in range(len(STREAM))
}

mapping = list(range(len(STREAM)))
distances = []

# Compute distances for all points
for i in range(len(STREAM)):
    for j in range(i + 1, len(STREAM)):
        c_dist = euclidian_dist_3D(STREAM[i], STREAM[j])
        distances.append([c_dist, i, j])

# Sort distances for 
distances.sort(key=lambda x: x[0])

while True:
    c_dists = distances.pop(0)
    min_distance = c_dists[0]

    # Get the next element in the list
    i += 1

    # plugged cable together
    path_ini, path_dest = c_dists[1], c_dists[2] 

    # If both cable are plugged together continue
    if mapping[path_ini] == mapping[path_dest]:
        continue

    # Save last plugged
    last_plugged = (path_ini, path_dest)
    plugged[mapping[path_ini]].extend(plugged[mapping[path_dest]])
    del plugged[mapping[path_dest]]

    # replace the second plug by the base
    next_path_dest = path_dest

    # Map mapping to update the current value
    for elem in range(len(mapping)):
        # If initial path is already pointed
        if elem != path_dest and mapping[elem] == mapping[path_dest]:
            mapping[elem] = mapping[path_ini]

    # Update mapping list
    mapping[path_dest] = mapping[path_ini]

    # If everything is plugged exit
    if len(plugged) == 1:
        break

print(STREAM[last_plugged[0]][0] * STREAM[last_plugged[1]][0])
# SOLUTION 1
# biggest_sol = [-1] * 3
# # Compute the final solution
# for elem in plugged.values():
#     insort(biggest_sol, len(elem))
#     biggest_sol.pop(0)

# print(biggest_sol[0] * biggest_sol[1] * biggest_sol[2])
