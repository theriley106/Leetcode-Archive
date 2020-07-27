class Solution(object):

    def topKFrequent(self, nums, k):
        a = {}
        for val in nums:
            if (str(val) not in a):
                a[str(val)] = 0
            a[str(val)] += 1
        correctVals = sorted(a.values())[(- k):]
        return [int(val) for val in a.keys() if (a[val] in correctVals)]