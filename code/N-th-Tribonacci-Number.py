class Solution(object):

    def __init__(self):
        self.db = {}

    def tribonacci(self, n):
        if (n < 1):
            return 0
        elif (n < 2):
            return 1
        elif (n == 2):
            return 1
        elif (n in self.db):
            return self.db[n]
        else:
            x = 0
            for i in xrange(1, 4):
                self.db[(n - i)] = self.tribonacci((n - i))
                x += self.db[(n - i)]
            return x