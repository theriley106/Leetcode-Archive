import random


class Solution(object):

    def search(self, nums, target):
        toAdd = 0
        low = 0
        high = len(nums)
        a = ((low + high) / 2)
        while ((nums[a] != target) and (high != low)):
            if (nums[a] > target):
                high = a
            elif (nums[a] < target):
                low = a
            else:
                return a
            prev = a
            a = ((low + high) / 2)
            if (a == prev):
                return (-1)
        return a
