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
                    undecided, cont = b.walkroom(path)
                    b.executed += 1
                    if not undecided and not cont:
                        if i == len(path_string) - 1:
                            b.printRoom()
                            print("(undecided: executed %d moves out of %d)" % (b.executed, len(path_string)))
                            break
                        continue
                    # else:
                    #     continue
                    if cont:
                        b.printRoom()
                        print("(win: executed %d moves out of %d)" % (b.executed, len(path_string)))
                        break
                    else:
                        b.printRoom()
                        print("(lose: executed %d moves out of %d)" % (b.executed, len(path_string)))
                        # break
                        break

            else:
                print("please enter a valid input")
        else:
            print ("You haven't provided any path!!")


gc.collect()
