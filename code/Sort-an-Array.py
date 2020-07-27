class Solution(object):

    def sortArray(self, nums):

        def qs(nums):
            if (len(nums) <= 1):
                return nums
            pivot = random.choice(nums)
            lessThan = [v for v in nums if (v < pivot)]
            eq = [v for v in nums if (v == pivot)]
            greatThan = [v for v in nums if (v > pivot)]
            return ((qs(lessThan) + eq) + qs(greatThan))
        return qs(nums)