class Solution(object):

    def xorOperation(self, n, start):
        nums = []
        i = 0
        v = 0
        while (len(nums) != n):
            v = (v ^ (start + (2 * i)))
            nums.append(1)
            i += 1
        return v