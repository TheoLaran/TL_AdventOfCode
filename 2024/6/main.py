#!/bin/python3
def get_data() -> list:
    """
        Return: List of each lines reads from inputs
    """
    # with open("little_dummy.txt", "r") as f:
    with open("dummy.txt", "r") as f:
    # with open("data.txt", "r") as f:
        return [line[:-1] for line in f]

PART_ONE = False
res = 0
data = get_data()
###############################################################################

def integer_to_pnt(itg, nb_cols):

    itg &= (~0xF)
    pnt_int = itg >> 4
    return pnt_int % nb_cols, pnt_int // nb_cols

def point_to_integer(pnt, nb_cols, sens):
    # Sens +1 on 4 bits
    sens_val = ((sens[0] + 1) << 2) + (sens[1] + 1)
    # Point integer computation
    pnt_int = pnt[0] + pnt[1] * nb_cols

    return (pnt_int << 4) + sens_val


def compute_next_dir(dct):
    
    if dct[0] == 0:
        x = -dct[1]
        y = 0
    else:
        y = dct[0]
        x = 0
    return (x, y)

for d in [(0,1),
          (0,-1),
          (-1,0),
          (1, 0)
          ]:
    print(f"{d=}, nd={compute_next_dir(d)}")


STR_TO_DIRECTION = {
        "^": (0,-1),
        "v": (0,1),
        "<": (-1,0),
        ">": (1, 0)
}

# Init map parameters
next_dct = (0,0)
###
curr_pnt = (0,0)
###
NB_COLS = len(data[0])
###
NB_ROWS = len(data)

for i, line in enumerate(data):
    for key in STR_TO_DIRECTION:
        # If the key is not in the line do nothing
        if key not in line:
            continue
        # otherwise update parameters
        curr_pnt = (line.find(key), i)
        next_dct = STR_TO_DIRECTION[key]              

DEBUG = True
PART_ONE = False
visited = set()
cross = []
while True:

    # if data[curr_pnt[1]][curr_pnt[0]] != "X": 
    
    itg = point_to_integer(curr_pnt, NB_COLS, (-1, -1))
    # Compute next position
    x, y =  curr_pnt[0] + next_dct[0], curr_pnt[1] + next_dct[1] 
    if itg not in visited:
        visited.add(itg)
        if PART_ONE:
            res += 1
        else:
            v = compute_next_dir(next_dct)
            # TODO: do that until reach # or out of bound
            tmp = curr_pnt[0], curr_pnt[1]
            # If out of bound exit
            while True:
                tmp = tmp[0] + v[0], tmp[1] + v[1]
                if tmp[0] < 0 or tmp[0] >= NB_COLS or tmp[1] < 0 or tmp[1] >= NB_ROWS:
                    break

                tmp_itg = point_to_integer(tmp , NB_COLS, v)
                # If we already visit it break
                if tmp_itg in visited:
                    # Compute position for obstacle  
                    tmp_itg = point_to_integer((x, y), NB_COLS, v)
                    dir_visited.add(tmp_itg & (~0xF))
                
                # otherwise continue:
                continue
        # data[curr_pnt[1]] = data[curr_pnt[1]][:curr_pnt[0]] + "X" + data[curr_pnt[1]][curr_pnt[0] + 1:]  

    
    # If we are out of bound guards exist, stop here
    if x < 0 or x >= NB_COLS or y < 0 or y >= NB_ROWS:
        break

    next_chr = data[y][x]
    ###
    if next_chr == "#":
        # print("\n".join(data))
        # print("\n" + "-" * 80 + "\n")
        next_dct = compute_next_dir(next_dct)
        if not PART_ONE:
            cross.append((curr_pnt, next_dct))
    else:
        curr_pnt = (x,y)
###############################################################################
print(res)
