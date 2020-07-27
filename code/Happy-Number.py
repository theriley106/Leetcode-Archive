class Solution(object):

    def isHappy(self, n, prev=[]):
        nums = sum([(int(x) ** 2) for x in list(str(n))])
        if (nums in prev):
            return False
        return (self.isHappy(nums, (prev + [nums])) if (nums != 1) else True)