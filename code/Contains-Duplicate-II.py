class Solution(object):

    def containsNearbyDuplicate(self, nums, k):
        a = {}
        for (i, val) in enumerate(nums):
            if (val not in a):
                a[val] = []
            a[val].append(i)
        for (key, val) in a.iteritems():
            if (len(val) > 1):
                x = sorted(val)
                for i in range((len(x) - 1)):
                    print abs((x[(i + 1)] - x[i]))
                    if (abs((x[(i + 1)] - x[i])) <= k):
                        return True
        return False