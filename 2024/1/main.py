def get_data() -> list:
    """
        Return: List of each lines reads from inputs
    """
    # with open("dummy.txt", "r") as f:
    with open("data.txt", "r") as f:
        return [line[:-1] for line in f]
data = get_data()

left = []
right = {}
for inp in data:
    sp = inp.strip().split()
    left.append(int(sp[0])) 
    spr = int(sp[1])
    if spr in right:
        right[spr] += 1
    else:
        right[spr] = 1

print(left, right)
print(sum(map(lambda x: abs(x * right.get(x, 0)), left)))
