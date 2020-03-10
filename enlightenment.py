import gc
from util import path_dict, short_distance


def move_forward(b):
    first_move = short_distance(b.brynjolf, b.exit)
    (px, py) = path_dict[first_move[0]]
    tx = b.x + px
    ty = b.y + py
    b.sol_path = b.sol_path + first_move[0]
    if b.solve_room(tx, ty):
        b.move_guard(px, py)
        b.printRoom()
        b.printSolution()
        print ("win: %s" % b.sol_path)
    else:
        b.printRoom()
        b.printSolution()
        print ("stuck: no way to win")


def enlightenment(b):
    path_string = input("Enter the path (Example: lrud): ")
    path_list = [i.lower() for i in list(path_string)]
    if (path_list and len(path_list) > 0):
        if "l" in path_list or "r" in path_list or "u" in path_list or "d" in path_list:
            for i, path in enumerate(path_list):
                undecided, cont = b.walkroom(path)
                b.executed += 1
                if not undecided and not cont:
                    if i == len(path_string) - 1:
                        b.printRoom()
                        # print("(undecided: executed %d moves of %d)" % (b.executed, len(path_string)))
                        break
                    else:
                        continue
                # else:
                #     continue
                if cont:
                    b.printRoom()
                    print ("win: %s" % b.sol_path)
                    break
                else:
                    if i == len(path_string) - 1:
                        b.printRoom()
                        print ("stuck: no way to win")
                        # break
                        break
                    else:
                        continue
            move_forward(b)
        else:
            print ("please enter a valid input")
        return 0
    else:
        move_forward(b)
    return 0


gc.collect()
