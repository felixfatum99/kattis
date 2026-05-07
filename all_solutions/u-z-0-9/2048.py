class game:
    board = None

    def move_left(self):
        for i in range(4):
            for j in range(3):
                if self.board[i][j] == 0:
                    self.board[i][j] = self.board[i][j+1]
                    self.board[i][j+1] = 0
                if j != 0 and self.board[i][j] == self.board[i][j-1]:
                    self.board[i][j-1] = self.board[i][j]*2
                    self.board[i][j] = 0
                if self.board[i][j] == 0:
                    self.board[i][j] = self.board[i][j+1]
                    self.board[i][j+1] = 0

    def set_board(self, b):
        self.board = b

    def print_board(self):
        for i in range(4):
            print(self.board[i][0],self.board[i][1],self.board[i][2],self.board[i][3] )


def run():
    g = game()
    b = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
    
    for i in range(4):
        x = input().split(" ")
        b[i][0] = int(x[0])
        b[i][1] = int(x[1])
        b[i][2] = int(x[2])
        b[i][3] = int(x[3])
    
    g.set_board(b)

    move = input()

    if move == "0":
        g.move_left()
    elif move == "1":
        g.move_up()
    elif move == "2":
        g.move_right()
    else:
        g.move_down()

    g.print_board()

run()

