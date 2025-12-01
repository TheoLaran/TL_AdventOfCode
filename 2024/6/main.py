#!/bin/python3

def get_data() -> list:
    """
        Return: List of each lines reads from inputs
    """
    # with open("little_dummy.txt", "r") as f:
    with open("dummy.txt", "r") as f:
    # with open("data.txt", "r") as f:
        return [line[:-1] for line in f]

PART_ONE = True
res = 0
data = get_data()
###############################################################################

STR_TO_DIRECTION = {
        # Up
        0: (0,-1),
        # Right
        1: (1,0),
        # Down
        3: (0,1),
        # Left
        4: (-1, 0)
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
    for key in ["^", ">", "v", "<"]:
        # If the key is not in the line do nothing
        if key not in line:
            continue
        # otherwise update parameters
        curr_pnt = (line.find(key), i)
        curr_dir = (
            0 if key == "^" else (
                1 if key == ">" else (
                    2 if key == "v" else 3
                )
            )
        )

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
    end_x, end_y = x, y
    match curr_dir:
        case 0:
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
        
        case 2:
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

        case 3:
            # If not wall in this line break
            if y not in WALL_Y_TO_X:
                return None

            # Otherwise search first wall ahead
            next_walls_x = list(filter(lambda nx: nx < x, WALL_Y_TO_X[y]))
            if len(next_walls_x) == 0:
                return None
            else:
                end_x = next_walls_x[-1] + 1

        case 1:
            # If not wall in this line break
            if y not in WALL_Y_TO_X:
                return None
            
            # Otherwise search first wall ahead
            next_walls_x = list(filter(lambda nx: nx > x, WALL_Y_TO_X[y]))
            if len(next_walls_x) == 0:
                return None
            else:
                end_x = next_walls_x[0] - 1
        case _:
            raise Exception(f"Matching direction {curr_dir}")
    return (end_x, end_y), (curr_dir + 1) % 4

# hash wall to integer
def wall_to_integer(n_wall_pos, cdir):
    x, y = n_wall_pos
    return (x + y * NB_COLS) << 3 + cdir

def update_obstacles(d, x, y):
    global obstacles, founded

    n_wall = get_wall_pos(d, x, y)
    while n_wall is not None:
        if wall_to_integer(*n_wall) in obstacles:
            founded.add(x + (1 if d == 3 else (-1 if d == 1 else 0)) + \
                        (y + (1 if d == 0 else (-1 if d == 2 else 0))) * NB_COLS)
            return
        (npx, npy), nd = n_wall
        n_wall = get_wall_pos(nd, npx, npy)

obstacles = set()
founded = set()

while True:
    x, y = curr_pnt
    should_break = False
    
    # create dynamic list of point visited
    next_wall_pos = get_wall_pos(curr_dir, x, y)
    print(curr_dir, next_wall_pos)
    if next_wall_pos is None:
        end_y = y if (curr_dir == 1 or curr_dir == 3) else (-1 if curr_dir == 0 else NB_ROWS)
        end_x = x if (curr_dir == 0 or curr_dir == 2) else (-1 if curr_dir == 1 else NB_COLS)
        curr_dir = (curr_dir + 1) % 4
    else:
        curr_pnt, curr_dir = next_wall_pos
        end_x, end_y = curr_pnt

    # TODO: Browse all walls and check if we hit one already visited
    if x == end_x:
        for ny in range(y, end_y, (-1 if y > end_y else 1)):
            itg = x + ny * NB_COLS
            visited.add(itg)
            if PART_ONE:
                continue
            else:
                update_obstacles(curr_dir, x, ny)

    elif y == end_y:
        for nx in range(x, end_x, (-1 if x > end_x else 1)):
            itg = nx + y * NB_COLS
            visited.add(itg)
            if PART_ONE:
                continue
            else:
                update_obstacles(curr_dir, nx, y)                

    else:
        raise Exception(" Neither x and y are stable ! ")

    if next_wall_pos is None:
        break

###############################################################################
print(len(visited))
print(founded)

