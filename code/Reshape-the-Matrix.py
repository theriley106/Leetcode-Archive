class Solution(object):

    def matrixReshape(self, nums, r, c):
        if ((len(nums) * len(nums[0])) != (r * c)):
            return nums

        def get_new():
            if (len(nums[0]) == 0):
                nums.pop(0)
            return nums[0].pop(0)
        return [[get_new() for i in range(c)] for i in range(r)]