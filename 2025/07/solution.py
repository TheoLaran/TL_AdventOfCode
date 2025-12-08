
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
SOLUTION = 2

# Save the position of falling beams
beams_x_positions = set()

# Link every x curr position to his timeline
beams_x_timelines = {}

# Find the first beams in the list
beams_x_positions.add(STREAM[0].index("S"))

# Init timelines, at the beggining we have one only
beams_x_timelines[STREAM[0].index("S")] = 1

for i, line in enumerate(STREAM):
    print(f"{i}/{len(STREAM)}")
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

            # Create empty shell for next values
            if max(idx - 1, 0) not in beams_x_timelines:
                beams_x_timelines[max(idx - 1, 0)] = 0
            if min(idx + 1, len(line)) not in beams_x_timelines:
                beams_x_timelines[min(idx + 1, len(line))] = 0

            # Update these value with the current number of timelines
            beams_x_timelines[max(idx - 1, 0)] += beams_x_timelines[idx]
            ###
            beams_x_timelines[min(idx + 1, len(line))] += beams_x_timelines[idx]

            # We are on a splitter, delete current position after treatment
            beams_x_timelines[idx] = 0

ttl_timeline = 0
for x_tl in beams_x_timelines.values():
    ttl_timeline += x_tl


print(ttl_timeline)