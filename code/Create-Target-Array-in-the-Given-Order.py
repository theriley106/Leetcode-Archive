class Solution(object):

    def createTargetArray(self, nums, index):
        initialArray = []
        for i in range(len(nums)):
            initialArray.insert(index[i], nums[i])
        return initialArray