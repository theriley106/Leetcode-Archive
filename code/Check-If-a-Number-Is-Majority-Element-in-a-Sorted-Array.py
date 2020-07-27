class Solution(object):

    def isMajorityElement(self, nums, target):
        db = {}
        maxCount = 0
        maxVal = None
        for val in nums:
            if (val not in db):
                db[val] = 0
            db[val] += 1
        return (db.get(target, 0) > (len(nums) / 2))