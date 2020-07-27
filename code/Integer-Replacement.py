class Solution(object):

    def integerReplacement(self, n):

        def solve(n, iterations=0):
            if (n == 1):
                return iterations
            if ((n % 2) == 0):
                n = (n / 2)
                return solve(n, (iterations + 1))
            else:
                return min(solve((n + 1), (iterations + 1)), solve((n - 1), (iterations + 1)))
        return solve(n)