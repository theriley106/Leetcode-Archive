class Solution(object):

    def __init__(self):
        self.y = 0
        self.x = 0

    def up(self):
        self.y = (self.y + 1)

    def down(self):
        self.y = (self.y - 1)

    def right(self):
        self.x = (self.x + 1)

    def left(self):
        self.x = (self.x - 1)

    def judgeCircle(self, moves):
        for move in moves:
            if (move.upper() == 'U'):
                self.up()
            if (move.upper() == 'D'):
                self.down()
            if (move.upper() == 'R'):
                self.right()
            if (move.upper() == 'L'):
                self.left()
        if ((self.y == 0) and (self.x == 0)):
            return True
        else:
            return False