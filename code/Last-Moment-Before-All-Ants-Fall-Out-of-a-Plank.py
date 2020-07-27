class Solution(object):

    def getLastMoment(self, n, left, right):
        if (len(left) == 0):
            maxLeft = 0
        else:
            maxLeft = max(left)
        if (len(right) == 0):
            minRight = n
        else:
            minRight = min(right)
        return max((n - minRight), maxLeft)