l, u, r, d = (0, -1), (-1, 0), (0, 1), (1, 0)
path_dict = {
    "r": r, "l": l, "u": u, "d": d
}


class Brynjolf:
    """Brynjolf is a thief"""
    def __init__(self, room, brynjolf, guards, exit):
        self.SIZE = len(room)
        self.room = room
        self.brynjolf = (self.x, self.y) = brynjolf
        self.guards = guards
        self.exit = exit
        solution = [[0] * self.SIZE for _ in range(self.SIZE)]
        self.solution = solution
        self.steps = 0
        self.sol_path_list = []
        self.sol_path = ""
        self.inp_sol_path = ""

    def in_boundaries(self, x, y):
        if x >= 0 and y >= 0 and x < self.SIZE and y < self.SIZE:
            return True
        return False

    def is_valid(self, x, y):
        if self.in_boundaries(x, y) and self.solution[x][y] == 0 and self.room[x][y] == 0:
            return True
        return False

    def move_guard_rc(self, gx, gy, x, y):
        tgx, tgy = gx + x, gy + y
        if self.is_valid(tgx, tgy) and self.room[tgx][tgy] != "X":
            return tgx, tgy
        return gx, gy

    def move_guard(self, ax, ay):
        for i, g in enumerate(self.guards):
            gx, gy = g[0], g[1]
            self.room[gx][gy] = 0
            gx, gy = self.move_guard_rc(gx, gy, ax, ay)
            self.room[gx][gy] = "G"
            self.guards[i] = (gx, gy)

    def move_guard_back(self, last_position):
        path = path_dict[last_position]
        px, py = path[0], path[1]
        for i, g in enumerate(self.guards):
            gx, gy = g[0], g[1]
            self.room[gx - px][gy - py] = 0
            self.room[gx][gy] = "G"
            self.guards[i] = (gx, gy)

    def move_brynjolf_back(self, last_position):
        path = path_dict[last_position]
        px, py = path[0], path[1]
        self.room[self.x][self.y] = 0
        self.room[self.x - px][self.y - py] = "B"
        self.x, self.y = self.x - px, self.y - py

    def solve_room(self, sx, sy):
        '''
            if destination E is reached, Brynjolf got out
            destination is the 'E'xit block
        '''
        if self.room[sx][sy] == "E":
            self.room[self.x][self.y] = 0
            self.solution[sx][sy] = 2
            return True
        '''
            checking if we can visit in this block or not
            the indices of the block must be in the boundaries (0, SIZE-1)
            and solution[sx][sy] == 0 is making sure that the block is not already visited
            self.room[sx][sy] == 0 is making sure that the block is not blocked
        '''
        if self.is_valid(sx, sy):
            if (self.room[sx][sy] != "X" or self.room[sx][sy] != "G"):
                # if safe to visit then visit the block
                self.steps += 1
                self.solution[sx][sy] = 1
                self.room[self.x][self.y] = 0
                self.x, self.y = sx, sy
                self.room[sx][sy] = "B"
                # going right
                if self.solve_room(sx, sy + 1):
                    self.sol_path = self.sol_path + 'r'
                    self.move_guard(0, 1)
                    # print("--------")
                    return True
                # going left
                if self.solve_room(sx, sy - 1):
                    self.sol_path = self.sol_path + 'l'
                    self.move_guard(0, -1)
                    # print("--------")
                    return True
                # going up
                if self.solve_room(sx - 1, sy):
                    self.sol_path = self.sol_path + 'u'
                    self.move_guard(-1, 0)
                    # print("--------")
                    return True
                # going down
                if self.solve_room(sx + 1, sy):
                    self.sol_path = self.sol_path + 'd'
                    self.move_guard(1, 0)
                    # print("--------")
                    return True
                # backtracking
                self.steps -= 1
                self.solution[sx][sy] = 0
                self.room[sx][sy] = 0
                if self.sol_path:
                    self.move_guard_back(self.sol_path[-1])
                    self.move_brynjolf_back(self.sol_path[-1])
                self.sol_path = self.sol_path[:-1]
                return False
        return 0

    def walkroom(self, path):
        inp_sol_path = ''
        px, py = path_dict[path]
        wx = self.x + px
        wy = self.y + py
        '''
            if destination E is reached, Brynjolf got out
            destination is the 'E'xit block
        '''
        if self.room[wx][wy] == "E":
            self.room[self.x][self.y] = 0
            self.solution[wx][wy] = 1
            return True
        '''
            checking if we can visit in this block or not
            the indices of the block must be in the boundaries (0, SIZE-1)
            and solution[x][y] == 0 is making sure that the block is not already visited
            room[x][y] == 0 is making sure that the block is not blocked
        '''
        if self.is_valid(wx, wy):
            if (self.room[wx][wy] != "X" or self.room[wx][wy] != "G"):
                self.steps += 1
                # if safe to visit then visit the block
                self.solution[wx][wy] = 1
                self.room[self.x][self.y] = 0
                self.x, self.y = wx, wy
                self.room[wx][wy] = "B"
                inp_sol_path = inp_sol_path + path
                self.move_guard(px, py)
                return True
            self.solution[wx][wy] = 0
            self.room[wx][wy] = 0
            self.steps -= 1
            if inp_sol_path:
                self.move_guard_back(inp_sol_path[-1])
                self.move_brynjolf_back(inp_sol_path[-1])
            inp_sol_path = inp_sol_path[:-1]
            return False
        return 0
