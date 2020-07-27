class Solution(object):

    def countElements(self, arr):
        db = set(arr)
        count = 0
        for val in arr:
            if ((val + 1) in db):
                count += 1
        return count