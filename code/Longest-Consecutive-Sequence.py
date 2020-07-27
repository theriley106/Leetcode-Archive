class Solution(object):

    def longestConsecutive(self, nums):
        db = {}
        self.maxVal = 0
        for val in nums:
            if (val not in db):
                db[val] = 0
            db[val] += 1
        for val in nums:
            tempVal = val
            count = 1
            while ((tempVal - 1) in db):
                count += 1
                tempVal = (tempVal - 1)
            self.maxVal = max(self.maxVal, count)
        return self.maxVal