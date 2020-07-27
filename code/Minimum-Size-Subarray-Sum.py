class Solution(object):

    def minSubArrayLen(self, s, nums):
        r = []
        total = 0
        for val in nums:
            total += val
            r.append(total)

        def sliding_window(size):
            sumVal = None
            for i in range(0, (1 + (len(nums) - size))):
                if (i == 0):
                    sumVal = r[((i + size) - 1)]
                else:
                    sumVal = (r[((i + size) - 1)] - r[(i - 1)])
                if (sumVal >= s):
                    return True
            return False
        for i in range(1, (len(nums) + 1)):
            x = sliding_window(i)
            if (x == True):
                return i
        return 0