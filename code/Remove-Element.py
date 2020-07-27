class Solution(object):

    def removeElement(self, nums, val):
        for v in range(nums.count(val)):
            nums.remove(val)
        return len(nums)