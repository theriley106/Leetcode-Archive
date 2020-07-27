class Solution(object):

    def productExceptSelf(self, nums):
        g = []
        db = {}

        def product(nums, without=None):
            if (str(without) in db):
                return db[str(without)]
            a = 1
            for v in nums:
                a = (a * v)
            db[str(without)] = a
            return a
        for i in range(len(nums)):
            if (str(nums[i]) in db):
                g.append(db[str(nums[i])])
            else:
                x = list(nums)
                x.pop(i)
                g.append(product(x, nums[i]))
        return g