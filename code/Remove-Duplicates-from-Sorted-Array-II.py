class Solution(object):

    def removeDuplicates(self, nums):
        db = {}
        i = 0
        while (i < len(nums)):
            val = nums[i]
            if (val not in db):
                db[val] = 0
            db[val] += 1
            if (db[val] > 2):
                del nums[i]
            else:
                i += 1