# --- Constants ---#
INPUT_SHORT_PATH = "input_short.txt"
INPUT_PATH = "input.txt"
STREAM = ""

# --- Read content of input ---#
with open(INPUT_SHORT_PATH, "r") as inpf:
    STREAM = inpf.read()

# --- Main solution ---#
ttl_zero = 0
zero_overflow = 0
dial = 50

for value in STREAM.split("\n"):
    # --- split input to get direction and nb of movement ---#
    direction, *nb = value
    nb = int("".join(nb))

    # --- Keep last dial in case of 0 ---#
    last_dial = dial

    # --- Update dial value ---#
    dial += nb * (-1 if direction == "L" else 1)

    if dial < 0 or dial > 100:
        zero_overflow += abs(dial // 100)

        # If we were on zero and go negative
        # Or positive and on a round number remove one
        if (last_dial == 0 and dial < 0) or (dial > 0 and dial % 100 == 0):
            zero_overflow -= 1

    dial = dial % 100
    if dial == 0:
        ttl_zero += 1

print(ttl_zero, zero_overflow, zero_overflow + ttl_zero)
