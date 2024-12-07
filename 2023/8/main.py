PATHS = []
NETWORK = {}
def fill_network():
    with open("input", "r") as f:
        for line in f:
            line = line.replace(" ", "")
            line = line.replace("(", "")
            line = line.replace(")", "")
            l = line.split("=")
            NETWORK[l[0]] = l[1].replace("\n", "").split(",")
            if l[0][-1] == "A":
                PATHS.append(l[0])

steps = 0
CMD = "LRRLRRRLRLRLLRRLRLRLLRLRLRLLLLRRRLLRRRLRRRLRRRLLRLLRLRRLRLRLRRRLLLLRRLRLRRLRRLLRRRLRRLRLRRLRRLRRLRRLRLLRRLRRLLLLRLRLRRLLRRLLRRLRLLRLRRLRRLRRLRRRLRRLLLRRLRRRLRLRRRLLRLRRLRRRLRRLLRRRLRRLRLLRRLLRRLRRLRRRLRRLLRRLRRRLRLRLRLRLRLRRLRRLLRRRLRLRRLRRRLRLRLRLRLRLRRRLRRLRRRLLRRLRLLRRRLRRLRLLLLRRRLRRLRRRR"
fill_network()
while not all(map(lambda x : x[-1] == "Z", PATHS)):
    next_cmd = CMD[steps % len(CMD)]
    for i, path in enumerate(PATHS):
        nxt = NETWORK[path][0 if next_cmd == 'L' else 1]
        PATHS[i] = nxt
        steps += 1
print(steps)