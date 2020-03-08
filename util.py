import math


l, u, r, d = (0, -1), (-1, 0), (0, 1), (1, 0)
path_dict = {
    "r": r, "l": l, "u": u, "d": d
}


def find_character_index(room, char):
    ch_list = []
    for ix, row in enumerate(room):
        for iy, i in enumerate(row):
            if char != "E":
                if i == char:
                    ch_list.append((ix, iy))
            else:
                if i == char or i == "O":
                    ch_list.append((ix, iy))
    return ch_list


def revert_back(x, y, last_position, path_dict):
    path = path_dict[last_position]
    px, py = path[0], path[1]
    x, y = x - px, y - py
    return x, y


#  write a function to calculate 2D distance between 2 co-ordinates
#  sqrt((x2-x1)**2 + (y2-y1)**2)
def find_distance(brynjolf, exit):
    distance = math.sqrt(sum([math.pow(a - b, 2) for a, b in zip(brynjolf, exit)]))
    return distance


def short_distance(brynjolf, exit):
    all_possibilities = []
    for direction in path_dict.keys():
        result = (direction, find_distance(tuple(sum(x) for x in zip(brynjolf, path_dict[direction])), exit))
        all_possibilities.append(result)
    which_direction = min(all_possibilities, key=lambda x: x[1])
    return which_direction
