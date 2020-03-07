# Brynjolf problem
import sys
from room import Room
from brynjolf import Brynjolf, path_dict

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


def call_solve_room(path=None):
    global sol_path
    key = path if path else "r"
    (px, py) = path_dict[key]
    tx = x + px
    ty = y + py
    if (b.solve_room(tx, ty)):
        sol_path = b.sol_path + key
        b.move_guard(px, py)
        print ("---------------")
        print_room()
        print_solution()
        print ("Path: ", sol_path, "steps", steps)
        return True
    else:
        print ("---------------")
        print_room()
        print_solution()
        print("You are stuck!", "steps", steps)
        return False

# call_solve_room()
# b.solve_room(x, y)
room = b.room

path_string = input("Enter the path (Example: lrud): ")
path_list = [i.lower() for i in list(path_string)]

if (path_list and len(path_list) > 0):
    if "l" in path_list or "r" in path_list or "u" in path_list or "d" in path_list:
        is_stuck = False
        for i, path in enumerate(path_list):
            if i + 1 == len(path_list):
                (px, py) = path_dict[path]
                tx = x + px
                ty = y + py
                if not b.solve_room(tx, ty):
                    is_stuck = True
                    continue
            else:
                if b.walkroom(path):
                    is_stuck = False
                    continue
                else:
                    is_stuck = True
                    break
        if not is_stuck:
            print ("sol_path", sol_path)
        else:
            print("You are stuck!", "steps", steps)
    else:
        print("please enter a valid input")
else:
    call_solve_room()
