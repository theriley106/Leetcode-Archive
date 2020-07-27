class Solution(object):

    def decompressRLElist(self, nums):
        a = []
        while (len(nums) > 0):
            for i in range(nums.pop(0)):
                a.append(nums[0])
            nums.pop(0)
        return a