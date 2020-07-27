class Solution(object):

    def __init__(self):
        self.versions = []
        lowestBad = float('inf')

    def firstBadVersion(self, n):
        i = 0
        j = n
        while (i < j):
            middle = ((i + j) / 2)
            if (isBadVersion(middle) == False):
                i = (middle + 1)
            else:
                j = middle
        return i