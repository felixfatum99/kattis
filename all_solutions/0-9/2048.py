#https://open.kattis.com/problems/2048
class gameBoard:
    def __init__(self, board):
        self.board = board
    
    def move(self, m):
        if m == 0:
            self.move_left()
        if m == 1:
            self.move_up()
        if m == 2:
            self.move_right()
        if m == 3:
            self.move_down()

    def move_left(self):
        for i in range(4):
            for k in range(4):
                for j in range(0, 3):
                    if self.board[i][j] == 0:
                        self.board[i][j] = self.board[i][j+1]
                        self.board[i][j+1] = 0
        for i in range(4):
            for j in range(3):
                if self.board[i][j] == self.board[i][j+1]:
                    self.board[i][j] = self.board[i][j]*2
                    for k in range(j+1, 3):
                        self.board[i][k] = self.board[i][k+1]
                    self.board[i][3] = 0

    def move_right(self):
        for i in range(4):
            for k in range(4):
                for j in range(3, 0, -1):
                    if self.board[i][j] == 0:
                        self.board[i][j] = self.board[i][j-1]
                        self.board[i][j-1] = 0
        for i in range(4):
            for j in range(3, 0, -1):
                if self.board[i][j] == self.board[i][j-1]:
                    self.board[i][j] = self.board[i][j]*2
                    for k in range(j-1, 0, -1):
                        self.board[i][k] = self.board[i][k-1]
                    self.board[i][0] = 0

    def move_up(self):
        for i in range(4):
            for k in range(4):
                for j in range(0, 3):
                    if self.board[j][i] == 0:
                        self.board[j][i] = self.board[j+1][i]
                        self.board[j+1][i] = 0
        for i in range(4):
            for j in range(3):
                if self.board[j][i] == self.board[j+1][i]:
                    self.board[j][i] = self.board[j][i]*2
                    for k in range(j+1, 3):
                        self.board[k][i] = self.board[k+1][i]
                    self.board[3][i] = 0

    def move_down(self):
        for i in range(4):
            for k in range(4):
                for j in range(3, 0, -1):
                    if self.board[j][i] == 0:
                        self.board[j][i] = self.board[j-1][i]
                        self.board[j-1][i] = 0
        for i in range(4):
            for j in range(3, 0, -1): 
                if self.board[j][i] == self.board[j-1][i]:
                    self.board[j][i] = self.board[j][i]*2
                    for k in range(j-1, 0, -1):
                        self.board[k][i] = self.board[k-1][i]
                    self.board[0][i] = 0  

    def print_board(self):
        for i in range(4):
            print(" ".join(map(str, self.board[i])))

def run():
    board = []
    for _ in range(4):
        row = [int(x) for x in input().split()]
        board.append(row)
    game = gameBoard(board)
    move = int(input())
    game.move(move)
    game.print_board()

run()