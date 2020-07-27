class TicTacToe(object, ):

    def __init__(self, n):
        self.size = n
        self.size1 = (n - 1)
        self.board = [[' ' for i in range(n)] for i in range(n)]

    def move(self, row, col, player):
        self.board[row][col] = player
        rowWin = True
        diagWin1 = True
        diagWin2 = True
        diagWin3 = True
        diagWin4 = True
        columnWin = True
        for i in range(self.size):
            rowWin = ((self.board[row][i] == player) and rowWin)
            columnWin = ((self.board[i][col] == player) and columnWin)
            diagWin1 = ((self.board[i][i] == player) and diagWin1)
            diagWin2 = (
                (self.board[i][(self.size1 - i)] == player) and diagWin2)
            diagWin3 = ((self.board[(self.size1 - i)]
                         [(self.size1 - i)] == player) and diagWin3)
            diagWin4 = ((self.board[(self.size1 - i)]
                         [i] == player) and diagWin4)
        if (True in [diagWin1, diagWin2, diagWin3, diagWin4, rowWin, columnWin]):
            return player
        else:
            return 0
