class Solution(object):

    def checkSubarraySum(self, nums, k):

        def is_multiple(sumVal):
            if (k == 0):
                return (sumVal == 0)
            return ((sumVal % k) == 0)
        for i in range(len(nums)):
            sumVal = 0
            c = 0
            for e in range(i, len(nums)):
                c += 1
                sumVal += nums[e]
                if (is_multiple(sumVal) and (c > 1)):
                    return True