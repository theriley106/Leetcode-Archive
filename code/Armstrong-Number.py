class Solution(object):

    def isArmstrong(self, N):
        strN = str(N)
        x = 0
        for (i, val) in enumerate(strN):
            x += (int(val) ** len(strN))
        return (x == N)