class Solution(object):

    def maxNumberOfApples(self, arr):
        arr.sort()
        vals = 0
        count = 0
        for val in arr:
            if ((val + vals) < 5000):
                vals += val
                count += 1
            else:
                break
        return count