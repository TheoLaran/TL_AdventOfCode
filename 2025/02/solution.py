inp="269194394-269335492,62371645-62509655,958929250-958994165,1336-3155,723925-849457,4416182-4470506,1775759815-1775887457,44422705-44477011,7612653647-7612728309,235784-396818,751-1236,20-36,4-14,9971242-10046246,8796089-8943190,34266-99164,2931385381-2931511480,277-640,894249-1083306,648255-713763,19167863-19202443,62-92,534463-598755,93-196,2276873-2559254,123712-212673,31261442-31408224,421375-503954,8383763979-8383947043,17194-32288,941928989-941964298,3416-9716"
short_inp="11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

# Constants
TOTAL_INVALID_IDS = 0
SOLUTION = 2

def is_invalid_id(value):
    # Convert input to str to manage it after
    value = str(value)

    # get size of input to split
    size = len(value)

    if SOLUTION == 2:
        # Browse all patterns in case of solution 2
        for i in range(1, size // 2 + 1):
            # If the content of the value is a pattern, return True
            if value.replace(value[:i], "") == "":
                return True
    
    # For both solution, ensure that both part from the middle are equal
    return value[:size // 2] == value[size // 2:] 

# Browse the input
for val in inp.split(","):
    # Split value on dash and convert to int
    v1, v2 = map(int, val.split("-"))

    # Take all invalid index from v1 to v2
    TOTAL_INVALID_IDS += sum(filter(is_invalid_id, range(v1, v2 + 1)))


print(TOTAL_INVALID_IDS)
