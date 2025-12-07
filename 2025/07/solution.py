
# --- Constants ---#
INPUT_SHORT_PATH = "input_short.txt"
INPUT_PATH = "input.txt"
STREAM = ""
SPLITTER = "^"
# --- Read content of input ---#
with open(INPUT_PATH, "r") as inpf:
    STREAM = inpf.read().split("\n")

# --- Main solution ---#
ttl_split = 0
SOLUTION = 1

# Save the position of falling beams
beams_x_positions = set()

# Find the first beams in the list
beams_x_positions.add(STREAM[0].index("S"))

for line in STREAM:
    # Find all splitter on the line
    splitter_idx = [i for i, s in enumerate(line) if s == SPLITTER]

    for idx in splitter_idx:
        # If the index collapse with beams position
        if idx in beams_x_positions:
            # Remove the current idx
            beams_x_positions.remove(idx)

            # Add two new position in the set
            beams_x_positions.add(max(idx - 1, 0))
            ###
            beams_x_positions.add(min(idx + 1, len(line)))

            # Increase nb of split
            ttl_split += 1

print(ttl_split) 
