# --- Imports ---#
import numpy as np

# --- Constants ---#
INPUT_SHORT_PATH = "input_short_raw.txt"
INPUT_PATH = "input_raw.txt"
SOLUTION = 2
DELIMITER = "|"
# --- Read content of input ---#
with open(INPUT_PATH, "r") as inpf:
    STREAM = inpf.read().split("\n")

# --- Main solution ---#

operations = STREAM[:-1]
symbols = STREAM[-1]
i = 0

str_substitution = lambda string, idx, new_chr: string[:idx] + new_chr + string[idx + 1 :]

while i < len(symbols) - 1:
    i += 1

    # If it is an offset continue
    if symbols[i] == " ":
        continue

    # Otherwise place delimiter at this index for operations
    for j in range(len(operations)):
        operations[j] = str_substitution(operations[j], i - 1, DELIMITER)

# Remove white space in symbols.
symbols = symbols.replace(" ", "")

# Split operations on delimiter
operations = [ operation.split(DELIMITER) for operation in operations]

# Take the transpose to manage line
operations = np.array(operations).T

if SOLUTION == 1:
    # For first solution operations to compute will just be integer value.
    operations = [list(map(int, operation)) for operation in operations]

elif SOLUTION == 2:
    new_operations = []
    for operation in operations:
        cur_operations = []

        # All string has the same size due to padding
        for idx in range(0, len(operation[0])):
            # Create new operation
            new_operation = ""
            for op in operation:
                new_operation += op[idx]

            # Append the new value to the list of new_operations
            cur_operations.append(int(new_operation.replace(" ", "")))

        # Append current operation to list of all operations to compute    
        new_operations.append(cur_operations)

    # Update operations list
    operations = new_operations    

# Compute operations depending on the symbols     
res = 0
for i, operation in enumerate(operations):
    res += sum(operation) if symbols[i] == "+" else np.prod(operation)

print(res)
