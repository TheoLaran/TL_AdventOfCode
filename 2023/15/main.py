ipt = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
def read_input():
    global ipt
    with open("input", "r") as f:
        for line in f:
            ipt = line

def hash_algo(string):
    value = 0
    for letter in string:
        value += ord(letter)
        value *= 17
        value = value % 256
    return value
read_input()
BOXES = [{} for _ in range(256)]

res = []
for string in ipt.split(","):
    
    if string[-1] == "-":
        box_id = hash_algo(string[:-1])
        BOXES[box_id].pop(string[:-1], None)
    else:
        l_string = string.split("=")
        box_id    = hash_algo(l_string[0])
        box_value = int(l_string[1])
        BOXES[box_id][l_string[0]] = box_value

res = []
for i, box in enumerate(BOXES):
    res.append(sum((i + 1) * (j + 1) * v for j, (_, v) in enumerate(box.items())))

print(sum(res))