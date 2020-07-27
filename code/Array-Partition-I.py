class Solution(object):

    def arrayPairSum(self, nums):
        a = sorted(nums)
        e = 0
        while (len(a) > 1):
            t = []
            try:
                t.append(a.pop(0))
                t.append(a.pop(0))
            except:
                pass
            e += min(t)
        return e