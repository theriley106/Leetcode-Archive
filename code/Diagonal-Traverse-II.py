class Solution(object):

    def findDiagonalOrder(self, nums):
        self.array = []
        self.vals = []
        self.db = {}
        for i in range(len(nums)):
            for e in range(len(nums[i])):
                if ((i + e) not in self.db):
                    self.db[(i + e)] = []
                self.db[(i + e)].append(nums[i][e])
                self.vals.append('{}_{}'.format(i, e))
        keyVals = sorted(self.db.keys())
        for i in keyVals:
            while (len(self.db[i]) > 0):
                self.array.append(self.db[i].pop((-1)))
        return self.array