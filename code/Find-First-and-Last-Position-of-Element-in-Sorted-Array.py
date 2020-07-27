class Solution(object):

    def searchRange(self, nums, target):
        if (target not in nums):
            return [(-1), (-1)]
        found = False
        first = None
        last = None
        for (i, val) in enumerate(nums):
            if (val == target):
                if (found != True):
                    found = True
                    first = i
                elif ((len(nums) - 1) == i):
                    last = i
            elif ((found == True) and (last == None)):
                last = (i - 1)
        if (last == None):
            last = first
        return [first, last]