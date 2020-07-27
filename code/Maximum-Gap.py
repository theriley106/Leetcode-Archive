import random


class Solution(object):

    def maximumGap(self, nums):
        diff = 0

        def qs(listVal):
            if (len(listVal) < 2):
                return listVal
            v = random.choice(listVal)
            lt = [x for x in listVal if (x < v)]
            gt = [x for x in listVal if (x > v)]
            return ((qs(lt) + [x for x in listVal if (x == v)]) + qs(gt))
        nums = qs(nums)
        for i in range((len(nums) - 1)):
            if (abs((nums[i] - nums[(i + 1)])) > diff):
                diff = abs((nums[i] - nums[(i + 1)]))
        return diff
