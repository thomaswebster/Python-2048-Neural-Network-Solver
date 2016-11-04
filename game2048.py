from random import choice, random
from copy import deepcopy

class GAME2048(object):
    def __init__(self):
        self.score = 0
        self.board = [[0]*4 for i in range(4)]
        self.spawn_value()

    def update(self, direction):
        if self.play_move(direction):
            self.spawn_value()

    def get_highest(self):
        return self.board[k] for k in range(4)
        it = 0
        for i in self.board:
            for j in i:
                if j > it:
                    it = j
        return it

    def check_board(self):
        def check_rows(board):
            for i in board:
                for j in range(len(i) - 1):
                    if i[j] == i[j+1]: 
                        return True
            return False

        for i in self.board:
            if 0 in i:         
                return True

        if check_rows(self.board): return True
        if check_rows(list(zip(*self.board))): return True

        return False

    def spawn_value(self):
        zero_indexes = []
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    zero_indexes.append([i,j])
        if zero_indexes:
            spawn_point = choice(zero_indexes)
            self.board[spawn_point[0]][spawn_point[1]] = 1 if random()>0.1 else 2

    def play_move(self, direction):
        if direction not in ["w","s","a","d"]: 
            print("not a valid input!")
            return False
        else:
            changed = deepcopy(self.board)
            self.illegal_moves = 0

            if direction == "w":
                self.board = list(map(list, list(zip(*self.board))))
                self.board_merge()
                self.board = list(map(list, list(zip(*self.board))))
            if direction == "s":
                self.board = list(map(list, list(zip(*self.board))))
                self.board = [list(reversed(row)) for row in self.board]
                self.board_merge()
                self.board = [list(reversed(row)) for row in self.board]
                self.board = list(map(list, list(zip(*self.board))))
            if direction == "a":
                self.board_merge()
            if direction == "d":
                self.board = [list(reversed(row)) for row in self.board]
                self.board_merge()
                self.board = [list(reversed(row)) for row in self.board]

            if changed == self.board: 
                self.illegal_moves += 1
                #print("Illegal Move!")
                return False
            return True

    def board_merge(self):
        def row_merge(row):
            def shift_zeros(row):
                temp_row = row

                for j in range(4):
                        if row[j] == 0:
                            temp_row.remove(0)
                            temp_row.append(0)

                return temp_row

            row = shift_zeros(row)

            for k in range(3):
                if row[k] == row[k+1] and row[k] != 0:
                    row[k] += 1
                    row[k+1] = 0

            row = shift_zeros(row)

            return row

        for i in range(4):
            self.board[i] = row_merge(self.board[i])

    def print_board(self):
        for i in self.board:
            print(i)

