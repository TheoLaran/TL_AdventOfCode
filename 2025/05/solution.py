
# --- Constants ---#
INPUT_SHORT_PATH = "input_short.txt"
INPUT_PATH = "input.txt"
STREAM = ""

# --- Read content of input ---#
with open(INPUT_PATH, "r") as inpf:
    STREAM = inpf.read()


# Pass Stream as two list, id_range and ids. Split on empty line
IDS_RANGE, IDXS = STREAM.split("\n\n")

# Generate list of SORTED_ID_RANGE, that will be sorted.
SORTED_IDS_RANGE = sorted(
    map(
        lambda x: (int(x.split("-")[0]), int(x.split("-")[1])),
        IDS_RANGE.split("\n")
    )
)

# Map index as integer
IDXS = map(int, IDXS.split("\n"))

# --- Main solution ---#
ttl_fresh = 0
SOLUTION = 2

if SOLUTION == 1:
    # Browse all ids and compute fresh one
    for idx in IDXS:
        i = 0
        while i < len(SORTED_IDS_RANGE):
            # If the food is in the current range add a fresh element and break
            if idx >= SORTED_IDS_RANGE[i][0] and idx <= SORTED_IDS_RANGE[i][1]:
                ttl_fresh += 1
                break
            i += 1

ttl_fresh = 0
if SOLUTION == 2:
    i = 0
    while i < len(SORTED_IDS_RANGE):
        min_id_fresh = SORTED_IDS_RANGE[i][0]
        max_id_fresh = SORTED_IDS_RANGE[i][1]
        
        # Compute overlaps
        while i < (len(SORTED_IDS_RANGE) - 1) and max_id_fresh >= SORTED_IDS_RANGE[i + 1][0]:
            i += 1

            # Take the new upper bound
            max_id_fresh = max(SORTED_IDS_RANGE[i][1], max_id_fresh)

        i += 1

        # Increase the nb of id by the nb of element in the range.
        ttl_fresh += max_id_fresh - min_id_fresh + 1

print(ttl_fresh) 
