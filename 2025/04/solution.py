
# --- Constants ---#
INPUT_SHORT_PATH = "input_short.txt"
INPUT_PATH = "input.txt"
STREAM = ""

# --- Read content of input ---#
with open(INPUT_PATH, "r") as inpf:
    STREAM = inpf.read().split("\n")

# --- Main solution ---#
ttl_forklifts = 0
nb_line = len(STREAM)
nb_col  = len(STREAM[0])

SOLUTION = 2
while True:
    nb_removed = 0
    for index_y, line in enumerate(STREAM):
        for index_x, value in enumerate(line):
            # If it is a dot nothing to do
            if value == ".":
                continue

            # build line of rolls using 8 around values
            roll_line = []
            for x in range(max(index_x - 1, 0), min(index_x + 2, nb_col)):
                for y in range(max(index_y - 1, 0), min(index_y + 2, nb_line)):
                    if (x, y) == (index_x, index_y):
                        continue
                    roll_line.append(STREAM[y][x])

            # If there if less than four roll remove the current status
            if roll_line.count("@") < 4:
                nb_removed += 1
                STREAM[index_y] = STREAM[index_y][:index_x] + "." + \
                                STREAM[index_y][min(index_x + 1, nb_col):]

    ttl_forklifts += nb_removed
    if SOLUTION == 1 or nb_removed == 0:
        break

print(ttl_forklifts)