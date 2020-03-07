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
