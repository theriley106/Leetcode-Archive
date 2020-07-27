class Solution(object):

    def repeatedStringMatch(self, A, B):
        count = 1
        while (B not in (A * count)):
            count += 1
            if ((len(A) * count) > 10000):
                return (-1)
        return count