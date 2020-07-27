class Solution(object):

    def rangeSum(self, nums, n, left, right):
        self.all = []

        def test(nums, vals=[], sumVal=0):
            if (len(vals) > 0):
                self.all.append(sumVal)
            if (len(nums) == 0):
                return
            test(nums[1:], (vals + [nums[0]]), (sumVal + nums[0]))
        for i in xrange(len(nums)):
            test(nums[i:])
        return sum(sorted(self.all)[(left - 1):right])