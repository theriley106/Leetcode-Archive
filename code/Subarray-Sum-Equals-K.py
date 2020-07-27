class Solution(object):

    def subarraySum(self, nums, k):
        tempSum = 0
        count = 0
        db = {0: 1}
        for val in nums:
            tempSum += val
            if ((tempSum - k) in db):
                count += db[(tempSum - k)]
            if (tempSum not in db):
                db[tempSum] = 0
            db[tempSum] += 1
        return count