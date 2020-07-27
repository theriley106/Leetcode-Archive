class Solution(object):

    def fib(self, N):
        if (N == 1):
            return 1
        if (N == 0):
            return 0
        return (self.fib((N - 2)) + self.fib((N - 1)))