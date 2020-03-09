from util import path_dict, short_distance


def enlightenment(b):
    print "\n2. Enlightenment it is then\n"
    (x, y) = b.brynjolf
    path_string = raw_input("Enter the path (Example: lrud): ")
    path_list = [i.lower() for i in list(path_string)]
    if (path_list and len(path_list) > 0):
        if "l" in path_list or "r" in path_list or "u" in path_list or "d" in path_list:
            for i, path in enumerate(path_list):
                # print ("i, path", i, path)
                if i + 1 == len(path_list):
                    (px, py) = path_dict[path]
                    tx = x + px
                    ty = y + py
                    # b.steps += 1
                    if b.is_valid(tx, ty):
                        # b.solution[tx][ty] = 1
                        # b.room[b.x][b.y] = 0
                        # b.x, b.y = tx, ty
                        # b.room[tx][ty] = "B"
                        if b.solve_room(tx, ty):
                            b.printRoom()
                            print "win: %s" % b.sol_path
                            break
                        else:
                            b.steps -= 1
                            b.solution[tx][ty] = 0
                            b.printRoom()
                            print "stuck: no way to win"
                            break
                    else:
                        print "stuck: no way to win"
                else:
                    _, cont = b.walkroom(path)
                    if cont:
                        b.printRoom()
                    else:
                        b.printRoom()
                        print "stuck: no way to win"
                        break
        else:
            print "please enter a valid input"
        return 0
    else:
        # print(short_distance(b.brynjolf, b.exit))
        first_move = short_distance(b.brynjolf, b.exit)
        # print ("first_move", first_move)
        (px, py) = path_dict[first_move[0]]
        tx = x + px
        ty = y + py
        b.sol_path = b.sol_path + first_move[0]
        b.move_guard(px, py)
        if b.solve_room(tx, ty):
            print "win: ", b.sol_path
        else:
            print "stuck: no way to win"
    return 0
