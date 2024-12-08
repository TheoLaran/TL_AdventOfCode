#!python3
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

ANTENAS = {}
NB_ROWS = len(data)
NB_COLS = len(data[0])
for j, line in enumerate(data):
    for i, char in enumerate(line):
        if char == ".":
            continue
        if char not in ANTENAS:
            ANTENAS[char] = []
        ANTENAS[char].append((i,j))

for _, positions in ANTENAS.items():
    for i, curr_pos in enumerate(positions):
        for other_pos in (positions[:i] + positions[i + 1:]):

            # Compute euclidian distance between current point and next antenna 
            xdiff =  other_pos[0] - curr_pos[0]
            ###
            ydiff =  other_pos[1] - curr_pos[1]
            
            # Compute next signal position using the distance
            next_pos = (other_pos[0] + xdiff, other_pos[1] + ydiff)

            # Update data until out of bound for part 2 
            while not(
                next_pos[0] < 0 or\
                next_pos[1] < 0 or\
                next_pos[0] >= NB_COLS or\
                next_pos[1] >= NB_ROWS
            ):

                # If this point does not contains signal increment res and continue
                if data[next_pos[1]][next_pos[0]] != "#":
                    res += 1
                    ###
                    data[next_pos[1]] = insert_in_string(
                        data[next_pos[1]],
                        "#",
                        next_pos[0]
                    )

                # If part one stop iteration here
                if PART_ONE:
                    break
            
                # Otherwise considere current signal as antenna and continue
                next_pos = (next_pos[0] + xdiff, next_pos[1] + ydiff)

# Add non overlapping T antenna position after run
for _, positions in ANTENAS.items():
    # Add all non overlapping antennas
    res += sum((
            1 if data[y][x] != "#" else 0\
                for x, y in positions 
        ))

###############################################################################

print(res)
