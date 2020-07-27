class Solution(object):

    def sumZero(self, n):
        a = []
        for i in range((n - 1)):
            a.append(i)
        return (a + [(sum(a) * (-1))])