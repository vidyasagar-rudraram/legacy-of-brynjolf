from util import revert_back, find_distance, path_dict


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

    def printRoom(self):
        print("Room:")
        for row in self.room:
            print(row)

    def printSolution(self):
        print("Solution:")
        for row in self.solution:
            print(row)

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
            tgx, tgy = self.move_guard_rc(gx, gy, ax, ay)
            if self.in_boundaries(tgx, tgy) and self.room[tgx][tgy] == 0:
                gx, gy = tgx, tgy
                self.room[gx][gy] = "G"
                self.guards[i] = (gx, gy)
            else:
                self.room[gx][gy] = "G"

    def move_guard_back(self, last_position):
        for i, g in enumerate(self.guards):
            gx, gy = g[0], g[1]
            self.room[gx][gy] = 0
            tgx, tgy = revert_back(gx, gy, last_position, path_dict)
            if self.in_boundaries(tgx, tgy):
                gx, gy = tgx, tgy
                self.guards[i] = (gx, gy)
            self.room[gx][gy] = "G"

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
        find_distance(self.brynjolf, self.exit)
        if self.in_boundaries(sx, sy):
            if self.room[sx][sy] == "E":
                self.room[self.x][self.y] = 0
                self.solution[sx][sy] = 2
                self.printRoom()
                self.printSolution()
                return True
        else:
            return False
        '''
            checking if we can visit in this block or not
            the indices of the block must be in the boundaries (0, SIZE-1)
            and solution[sx][sy] == 0 is making sure that the block is not already visited
            self.room[sx][sy] == 0 is making sure that the block is not blocked
        '''
        if self.is_valid(sx, sy):
            return self.util_solve_room(sx, sy)
        return 0

    def util_solve_room(self, sx, sy):
        self.steps += 1
        self.solution[sx][sy] = 1
        self.room[self.x][self.y] = 0
        self.x, self.y = sx, sy
        self.room[sx][sy] = "B"
        # going right
        self.move_guard(0, 1)
        if self.solve_room(sx, sy + 1):
            self.sol_path = 'r' + self.sol_path
            return True
        else:
            if len(self.sol_path):
                self.move_guard_back(self.sol_path[-1])
                self.move_brynjolf_back(self.sol_path[-1])
        # going left
        self.move_guard(0, -1)
        if self.solve_room(sx, sy - 1):
            self.sol_path = 'l' + self.sol_path
            return True
        else:
            if len(self.sol_path):
                self.move_guard_back(self.sol_path[-1])
                self.move_brynjolf_back(self.sol_path[-1])
        # going up
        self.move_guard(-1, 0)
        if self.solve_room(sx - 1, sy):
            self.sol_path = 'u' + self.sol_path
            return True
        else:
            if len(self.sol_path):
                self.move_guard_back(self.sol_path[-1])
                self.move_brynjolf_back(self.sol_path[-1])
        # going down
        self.move_guard(1, 0)
        if self.solve_room(sx + 1, sy):
            self.sol_path = 'd' + self.sol_path
            return True
        else:
            if len(self.sol_path):
                self.move_guard_back(self.sol_path[-1])
                self.move_brynjolf_back(self.sol_path[-1])
        # backtracking
        self.steps -= 1
        self.solution[sx][sy] = 0
        # self.room[self.x][self.y] = "B"
        # self.room[sx][sy] = 0
        return False

    def walkroom(self, path):
        px, py = path_dict[path]
        wx = self.x + px
        wy = self.y + py
        '''
            if destination E is reached, Brynjolf got out
            destination is the 'E'xit block
        '''
        if self.in_boundaries(wx, wy):
            if self.room[wx][wy] == "E":
                self.room[self.x][self.y] = 0
                self.solution[wx][wy] = 2
                self.printRoom()
                self.printSolution()
                return True
        else:
            return False
        '''
            checking if we can visit in this block or not
            the indices of the block must be in the boundaries (0, SIZE-1)
            and solution[x][y] == 0 is making sure that the block is not already visited
            room[x][y] == 0 is making sure that the block is not blocked
        '''
        if self.is_valid(wx, wy):
            self.steps += 1
            # if safe to visit then visit the block
            self.solution[wx][wy] = 1
            self.room[self.x][self.y] = 0
            self.x, self.y = wx, wy
            self.room[wx][wy] = "B"
            self.inp_sol_path = self.inp_sol_path + path
            self.move_guard(px, py)
            self.printRoom()
            self.printSolution()
            return True
        return 0
