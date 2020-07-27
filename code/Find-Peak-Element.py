class Solution(object):

    def findPeakElement(self, nums):
        db = {}
        max_val = float('-inf')
        for (i, val) in enumerate(nums):
            if ((val not in db) and (val > max_val)):
                db[val] = i
                max_val = val
        return db[max_val]