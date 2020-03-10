from util import revert_back, path_dict


class Brynjolf:
    """Brynjolf is a thief"""
    def __init__(self, room, brynjolf, guards, exit):
        self.SIZE = len(room)
        self.room = room
        self.brynjolf = (self.x, self.y) = brynjolf
        self.guards = guards
        self.exit = exit
        self.solution = [[0] * self.SIZE for _ in range(self.SIZE)]
        self.steps = 0
        self.executed = 0
        self.undecided = False
        self.sol_path_list = []
        self.sol_path = ""
        self.inp_sol_path = ""

    def printRoom(self):
        print ("Room:")
        for row in self.room:
            print (row)

    def printSolution(self):
        print ("Solution:")
        for row in self.solution:
            print (row)

    def in_boundaries(self, x, y):
        if x >= 0 and y >= 0 and x < self.SIZE and y < self.SIZE:
            return True
        return False

    def is_valid(self, x, y):
        if self.in_boundaries(x, y) and self.solution[x][y] == 0 and self.room[x][y] == 0:
            return True
        return False

    def move_guard_xy(self, gx, gy, x, y):
        tgx, tgy = gx + x, gy + y
        if self.is_valid(tgx, tgy):
            return tgx, tgy
        return gx, gy

    def move_guard(self, ax, ay):
        for i, g in enumerate(self.guards):
            gx, gy = g[0], g[1]
            self.room[gx][gy] = 0
            tgx, tgy = self.move_guard_xy(gx, gy, ax, ay)
            if self.in_boundaries(tgx, tgy) and self.room[tgx][tgy] == 0:
                gx, gy = tgx, tgy
                self.room[gx][gy] = "G"
                self.guards[i] = (gx, gy)
            else:
                self.room[gx][gy] = "G"

    def move_guard_check(self, ax, ay):
        moved = False
        for i, g in enumerate(self.guards):
            gx, gy = g[0], g[1]
            self.room[gx][gy] = 0
            tgx, tgy = gx + ax, gy + ay
            if self.in_boundaries(tgx, tgy) and self.room[tgx][tgy] == 0:
                moved = True
                gx, gy = tgx, tgy
                self.room[gx][gy] = "G"
                self.guards[i] = (gx, gy)
            else:
                self.room[gx][gy] = "G"
        return moved

    def move_guard_back(self, last_position):
        for i, g in enumerate(self.guards):
            gx, gy = g[0], g[1]
            self.room[gx][gy] = 0
            tgx, tgy = revert_back(gx, gy, last_position, path_dict)
            if self.in_boundaries(tgx, tgy):
                gx, gy = tgx, tgy
                self.guards[i] = (gx, gy)
            self.room[gx][gy] = "G"

    def move_brynjolf(self, bx, by):
        self.room[self.x][self.y] = 0
        self.x, self.y = bx, by
        self.room[bx][by] = "B"

    def move_brynjolf_back(self, last_position):
        self.room[self.x][self.y] = 0
        (tx, ty) = revert_back(self.x, self.y, last_position, path_dict)
        if self.in_boundaries(tx, ty):
            self.x, self.y = tx, ty
        self.room[self.x][self.y] = "B"
        self.sol_path = self.sol_path[:-1]

    def solve_room(self, sx, sy):
        '''
            if destination E is reached, Brynjolf got out
            destination is the 'E'xit block
        '''
        if self.in_boundaries(sx, sy) and self.room[sx][sy] == "E":
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
            self.steps += 1
            self.solution[sx][sy] = 1
            # self.room[self.x][self.y] = 0
            # self.x, self.y = sx, sy
            # self.room[sx][sy] = "B"
            self.move_brynjolf(sx, sy)
            # going right
            if self.solve_room(sx, sy + 1):
                self.move_guard(0, 1)
                self.sol_path = 'r' + self.sol_path
                return True
            # going left
            if self.solve_room(sx, sy - 1):
                self.move_guard(0, -1)
                self.sol_path = 'l' + self.sol_path
                return True
            # going up
            if self.solve_room(sx - 1, sy):
                self.move_guard(-1, 0)
                self.sol_path = 'u' + self.sol_path
                return True
            # going down
            if self.solve_room(sx + 1, sy):
                self.move_guard(1, 0)
                self.sol_path = 'd' + self.sol_path
                return True
            # backtracking
            self.steps -= 1
            self.solution[sx][sy] = 0
            if len(self.sol_path):
                self.move_guard_back(self.sol_path[-1])
                self.move_brynjolf_back(self.sol_path[-1])
            return False
        return 0

    def walkroom(self, path):
        px, py = path_dict[path]
        wx = self.x + px
        wy = self.y + py
        '''
            if destination E is reached, Brynjolf got out
            destination is the 'E'xit block
        '''
        if self.in_boundaries(wx, wy) and self.room[wx][wy] == "E":
            self.room[self.x][self.y] = 0
            self.x, self.y = wx, wy
            self.solution[wx][wy] = 2
            return self.undecided, True
        '''
            checking if we can visit in this block or not
            the indices of the block must be in the boundaries (0, SIZE-1)
            and solution[x][y] == 0 is making sure that the block is not already visited
            room[x][y] == 0 is making sure that the block is not blocked
        '''
        self.undecided = True
        if self.in_boundaries(wx, wy) and self.room[wx][wy] == 0:
            self.inp_sol_path = self.inp_sol_path + path
            self.steps += 1
            # if safe to visit then visit the block
            self.solution[wx][wy] = 1
            self.room[self.x][self.y] = 0
            self.room[wx][wy] = "B"
            self.move_guard(px, py)
            self.x, self.y = wx, wy
            self.undecided = False
        else:
            if not self.move_guard_check(px, py):
                self.undecided = False
        return self.undecided, False
