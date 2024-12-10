#!/usr/bin/python3
def get_data() -> list:
    """
        Return: List of each lines reads from inputs
    """
    # with open("little_dummy.txt", "r") as f:
    # with open("dummy.txt", "r") as f:
    with open("data.txt", "r") as f:
        return [line[:-1] for line in f]

PART_ONE = False
res = 0
data = get_data()

def insert_in_string(string, value, index):
    if index == len(string):
        return string[:-1] + value
    return string[:index] + value + string[index + 1:]


################################################################################

class TrailHiking:
    def __init__(self, init_x, init_y, data):
        # Saves for this class
        self.visited = set()
        
        # SAve directions i.e. left, right top, left
        self.DIRECTIONS = [(-1,0),(1,0),(0,-1),(0,1)]

        # Setup point to visit s.t. = curr_point, id, path 
        from collections import deque
        ###
        self.to_visit = deque()
        ###
        self.to_visit.appendleft(((init_x, init_y), 0, []))

        self.achieves = set()
        pass

    def __is_out_of_boud(self, x, y):
        return x < 0 or y < 0 or y >= NB_COLS or x >= NB_ROWS
    
    def __point_to_integer(self, x, y):
        return x + y * NB_COLS
    
    def __path_to_integer(self, path):
        return len(self.achieves) + 1

    def __visit_next(self) -> None:
        point, id, path = self.to_visit.pop()

        for dir in self.DIRECTIONS:
            next_point = point[0] + dir[0], point[1] + dir[1]
            ###
            if self.__is_out_of_boud(*next_point):
                continue
            
            if data[next_point[1]][next_point[0]] == id + 1:
                if id == 8:
                    if PART_ONE:
                        self.achieves.add(self.__point_to_integer(*next_point))
                    else:
                        self.achieves.add(self.__path_to_integer(path))
                    continue
                # Save id for path
                ppti = self.__point_to_integer(*point)
                ###
                self.to_visit.appendleft((next_point, id + 1, path + [ppti]))
        
        return None
    
    def draw_path(self):
        # If we achieve a nine return all point browse by our class to update
        # global path
        pass

    def visit_all(self, debug = False) -> int:
        while len(self.to_visit) != 0:
            if debug:
                print(self.to_visit)
            self.__visit_next()
        return len(self.achieves)


# Convert data as int
data = list(list(map(int, d)) for d in data)
###
NB_ROWS = len(data)
###
NB_COLS = len(data[0])

to_visited = []


# Setup TrailHeads position
TRAILHEADS = {}
###
for i, line in enumerate(data):
    for j, th_id in enumerate(line):
        # If current th id not seen add it
        if th_id not in TRAILHEADS:
            TRAILHEADS[th_id] = []

        # Add x and y position in the TRAILHEADS
        TRAILHEADS[th_id].append((j, i))

        # If id is 0 mark it as to visited
        if th_id == 0:
            to_visited.append(TrailHiking(j, i, data))

        
res = sum(
    (
        th.visit_all()
        for th in to_visited
    )
)



###############################################################################

print(res)
