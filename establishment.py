from util import path_dict


def establishment(b):
    print ("\n1. Establishment it is then\n")
    (x, y) = b.brynjolf
    run = True
    while run:
        try:
            path_string = str(input("Please Enter the path (Example: lrud): "))
        except ValueError:
            print("Please input only Directions in string format")
            continue
        path_list = [i.lower() for i in list(path_string) if i]
        if (path_list and len(path_list) > 0):
            run = False
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
                            b.executed += 1
                            continue
                        else:
                            print("(lose: executed " + str(b.executed) + " moves of ", len(path_string))
                            break
            else:
                print("please enter a valid input")
        else:
            print ("You haven't provided any path!!")
        #     # print(short_distance(b.brynjolf, b.exit))
        #     if b.util_solve_room(x, y):
        #         print ("sol_path", b.sol_path, "steps", b.steps)
        #     else:
        #         print("You are stuck!", "steps", b.steps)
