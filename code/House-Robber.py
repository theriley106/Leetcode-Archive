class Solution(object):

    def rob(self, nums):
        db = {}
        self.a = [(-1) for i in range(len(nums))]

        def calc_all(index, cont=False):
            if (index >= len(nums)):
                return 0
            if (self.a[index] != (-1)):
                return self.a[index]
            a = (calc_all((index + 2)) + nums[index])
            b = (calc_all((index + 3)) + nums[index])
            self.a[index] = max(a, b)
            return self.a[index]
        db = {}
        return max(calc_all(0), calc_all(1))
        print calc_all(0)
        print self.a
        print calc_all(1)