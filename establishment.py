import gc


def establishment(b):
    (x, y) = b.brynjolf
    run = True
    while run:
        try:
            path_string = input("Please Enter the path (Example: lrud): ")
        except ValueError:
            print("Please input only Directions in string format")
            continue
        path_list = [i.lower() for i in list(path_string) if i]
        if (path_list and len(path_list) > 0):
            run = False
            if "l" in path_list or "r" in path_list or "u" in path_list or "d" in path_list:
                for i, path in enumerate(path_list):
                    # if len(path_list) > 1 and i + 1 == len(path_list):
                    #     (px, py) = path_dict[path]
                    #     tx = x + px
                    #     ty = y + py
                    #     if b.solve_room(tx, ty):
                    #         print ("(win: executed %d moves out of %d)" % (b.executed, len(path_string)))
                    #         break
                    #     else:
                    #         print("You are stuck!", "steps", b.steps)
                    #         break
                    # else:
                    #     undecided, cont = b.walkroom(path)
                    #     if undecided:
                    #         b.printRoom()
                    #         print("(undecided: executed %d moves of %d)" % (b.executed, len(path_string)))
                    #         break
                    #     else:
                    #         if cont:
                    #             b.executed += 1
                    #             b.printRoom()
                    #             print("(win: executed %d moves of %d)" % (b.executed, len(path_string)))
                    #             break
                    #         else:
                    #             b.printRoom()
                    #             # print("(lose: executed %d moves of %d)" % (b.executed, len(path_string)))
                    #             # break
                    #             continue
                    # print ("direction: %s" % path)
                    undecided, cont = b.walkroom(path)
                    # if undecided:
                    #     b.printRoom()
                    #     b.printSolution()
                    #     print("(undecided: executed %d moves of %d)" % (b.executed, len(path_string)))
                    #     break
                    # else:
                    #     if cont:
                    #         b.executed += 1
                    #         b.printRoom()
                    #         b.printSolution()
                    #         print("(win: executed %d moves of %d)" % (b.executed, len(path_string)))
                    #         break
                    #     else:
                    #         b.printRoom()
                    #         b.printSolution()
                    #         print("(lose: executed %d moves of %d)" % (b.executed, len(path_string)))
                    #         # break
                    #         continue
                    #     continue
                    b.executed += 1
                    # print ("undecided", undecided, "cont", cont)
                    if not undecided and not cont:
                        if i == len(path_string) - 1:
                            b.printRoom()
                            b.printSolution()
                            print("(undecided: executed %d moves of %d)" % (b.executed, len(path_string)))
                            break
                        continue
                    # else:
                    #     continue
                    if cont:
                        b.printRoom()
                        b.printSolution()
                        print("(win: executed %d moves of %d)" % (b.executed, len(path_string)))
                        break
                    else:
                        b.printRoom()
                        b.printSolution()
                        print("(lose: executed %d moves of %d)" % (b.executed, len(path_string)))
                        # break
                        break

            else:
                print("please enter a valid input")
        else:
            print ("You haven't provided any path!!")


gc.collect()
