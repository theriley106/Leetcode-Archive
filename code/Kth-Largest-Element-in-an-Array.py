import random


class Solution(object):

    def findKthLargest(self, nums, k):

        def qs(array):
            if (len(array) == 0):
                return []
            a = random.choice(array)
            eq = [g for g in array if (g == a)]
            gt = [g for g in array if (g > a)]
            lt = [g for g in array if (g < a)]
            return ((qs(gt) + eq) + qs(lt))
        a = qs(nums)
        return a[(k - 1)]
