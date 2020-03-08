# Brynjolf problem
import sys
from room import Room
from brynjolf import Brynjolf, path_dict
from util import short_distance

try:
    filePath = sys.argv[1]
except IndexError:
    filePath = input("Please enter a file name with the room: ")
    if not filePath:
        print ("No file provided. Using the defined Sample room.txt")
        filePath = 'room.txt'

r = Room(filePath)
(x, y) = r.brynjolf
b = Brynjolf(r.room, r.brynjolf, r.guards, r.exit)
print ("brynjolf", b.brynjolf)
print ("guards", b.guards)
print ("exit", b.exit)
solution = b.solution
steps = b.steps
sol_path = b.sol_path


# initially the room
def print_room():
    print ("Room:")
    for m in r.room:
        print(m)


def print_solution():
    print ("Solution:")
    for s in solution:
        print(s)


room = b.room
print_room()

path_string = input("Enter the path (Example: lrud): ")
path_list = [i.lower() for i in list(path_string)]

if (path_list and len(path_list) > 0):
    if "l" in path_list or "r" in path_list or "u" in path_list or "d" in path_list:
        for i, path in enumerate(path_list):
            if i + 1 == len(path_list):
                (px, py) = path_dict[path]
                tx = x + px
                ty = y + py
                if b.util_solve_room(tx, ty):
                    print ("uitl_solve_room sol_path", b.sol_path, "steps", b.steps)
                    break
                else:
                    print("util_solve_room You are stuck!", "steps", b.steps)
                    break
            else:
                if b.walkroom(path):
                    continue
                else:
                    print("walkroom You are stuck!", "steps", b.steps)
                    break
    else:
        print("please enter a valid input")
else:
    # print(short_distance(b.brynjolf, b.exit))
    if b.util_solve_room(x, y):
        print ("sol_path", b.sol_path, "steps", b.steps)
    else:
        print("You are stuck!", "steps", b.steps)
