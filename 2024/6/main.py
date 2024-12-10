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

STR_TO_DIRECTION = {
        "^": (0,-1),
        "v": (0,1),
        "<": (-1,0),
        ">": (1, 0)
}

DEBUG = True
PART_ONE = False
visited = set()
cross = []

import re
from bisect import insort_left

WALL_X_TO_Y = {}
###
WALL_Y_TO_X = {}

# Init map parameters
curr_dir = (0,0)
###
curr_pnt = (0,0)
###
NB_COLS = len(data[0])
###
NB_ROWS = len(data)
###

WALL_REGEX = "(?=#)"
for i, line in enumerate(data):
    for key in STR_TO_DIRECTION:
        # If the key is not in the line do nothing
        if key not in line:
            continue
        # otherwise update parameters
        curr_pnt = (line.find(key), i)
        curr_dir = key

    for wall_pos in re.finditer(WALL_REGEX, line):
        wp = wall_pos.start()

        if i not in WALL_Y_TO_X:
            WALL_Y_TO_X[i] = []
        
        if wp not in WALL_X_TO_Y:
            WALL_X_TO_Y[wp] = []
        
        insort_left(WALL_Y_TO_X[i], wp)
        insort_left(WALL_X_TO_Y[wp], i)

visited = set()

def get_wall_pos(curr_dir, x, y):
    curr_pnt = None
    end_x, end_y = x, y
    match curr_dir:
        case "^":
            # If not wall in this column break
            if x not in WALL_X_TO_Y:
                return None
            else:
                # Otherwise search first wall ahead
                next_walls_y = list(filter(lambda ny: ny < y, WALL_X_TO_Y[x]))
                if len(next_walls_y) == 0:
                    return None
                else:
                    end_y = next_walls_y[-1] + 1
                    curr_pnt = (end_x, end_y)
                    curr_dir = ">"
        
        case "v":
            # If not wall in this column break
            if x not in WALL_X_TO_Y:
                return None
            else:
                # Otherwise search first wall ahead
                next_walls_y = list(filter(lambda ny: ny > y, WALL_X_TO_Y[x]))
                if len(next_walls_y) == 0:
                    return None
                else: 
                    end_y = next_walls_y[0] - 1
                    curr_pnt = (end_x, end_y)
                    curr_dir = "<"

        case "<":
            # If not wall in this line break
            if y not in WALL_Y_TO_X:
                return None

            # Otherwise search first wall ahead
            next_walls_x = list(filter(lambda nx: nx < x, WALL_Y_TO_X[y]))
            if len(next_walls_x) == 0:
                return None
            else:
                end_x = next_walls_x[-1] + 1
                curr_pnt = (end_x, end_y)
                curr_dir = "^"

        case ">":
            # If not wall in this line break
            if y not in WALL_Y_TO_X:
                return None
            
            # Otherwise search first wall ahead
            next_walls_x = list(filter(lambda nx: nx > x, WALL_Y_TO_X[y]))
            if len(next_walls_x) == 0:
                return None
            else:
                end_x = next_walls_x[0] - 1
                curr_pnt = (end_x, end_y)
                curr_dir = "v"
    
    return curr_pnt, curr_dir

obstacles = set()

while True:
    x, y = curr_pnt
    should_break = False
    
    # create dynamic list of point visited

    next_wall_pos = get_wall_pos(curr_dir, x, y)

    if next_wall_pos is None:
        end_y = y if (curr_dir == "<" or curr_dir == ">") else (-1 if curr_dir == "^" else NB_ROWS)
        end_x = x if (curr_dir == "^" or curr_dir == "v") else (-1 if curr_dir == "<" else NB_COLS)
    else:
        curr_pnt, curr_dir = next_wall_pos
        end_x, end_y = curr_pnt

    if x == end_x:
        for ny in range(y, end_y, (-1 if y > end_y else 1)):
            itg = x + ny * NB_COLS
            visited.add(itg)
            if PART_ONE:
                continue
            else:
                nd = curr_dir
                npy = ny
                npx = x
                for _ in range(4):
                    n_wall = get_wall_pos(nd, npx, npy)
                    if n_wall is None:
                        break
                    (npx, npy), nd = n_wall
                else:
                    if npx == x and y <= npy <= end_y:
                        obstacles.add(x + ny * NB_COLS)
        
    elif y == end_y:
        for nx in range(x, end_x, (-1 if x > end_x else 1)):
            itg = nx + y * NB_COLS
            visited.add(itg)
            if PART_ONE:
                continue
            else:
                nd = curr_dir
                npy = y
                npx = nx
                for _ in range(3):
                    n_wall = get_wall_pos(nd, npx, npy)
                    if n_wall is None:
                        break
                    (npx, npy), nd = n_wall
                else:
                    if y == npy and npx == x:
                        obstacles.add(nx + y * NB_COLS)
                

    else:
        raise Exception(" Neither x and y are stable ! ")

    if next_wall_pos is None:
        break

###############################################################################
print(len(visited))
print(len(obstacles))
