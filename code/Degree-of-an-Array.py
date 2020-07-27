class Solution(object):

    def findShortestSubArray(self, nums):
        maxVals = []

        def calc_degree(num):
            x = nums.index(num)
            c = 0
            count = 0
            while (c != db[num]):
                if (nums[x] == num):
                    c += 1
                x += 1
                count += 1
            return count
        db = {}
        for v in nums:
            if (v not in db):
                db[v] = 0
            db[v] += 1
        maxVal = max(db.values())
        for (k, v) in db.iteritems():
            if (v == maxVal):
                maxVals.append(k)
        return min([calc_degree(val) for val in maxVals])