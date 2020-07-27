class Solution(object):

    def rotate(self, nums, k):
        for i in range(k):
            x = nums.pop((-1))
            nums.insert(0, x)