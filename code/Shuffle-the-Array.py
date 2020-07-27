class Solution(object):

    def shuffle(self, nums, n):
        e = []
        while (len(nums) > 0):
            r = (len(nums) / 2)
            a = nums.pop(0)
            b = nums.pop((r - 1))
            e.append(a)
            e.append(b)
        return e