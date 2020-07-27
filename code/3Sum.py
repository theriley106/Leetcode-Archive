class Solution(object):

    def threeSum(self, numz):
        db = {}
        db2 = {}
        nums = []
        for val in numz:
            if (val not in db):
                db[val] = 0
            db[val] += 1
            if (db[val] < 4):
                nums.append(val)

        def all_in(threeVals):
            temp = {}
            for val in threeVals:
                if (val not in temp):
                    temp[val] = 0
                temp[val] += 1
                if (temp[val] > db[val]):
                    return False
            return threeVals
        a = []
        b = {}
        for i in xrange(len(nums)):
            for e in xrange(i, len(nums)):
                if ((0 - (nums[i] + nums[e])) in db):
                    v = [nums[i], nums[e], (0 - (nums[i] + nums[e]))]
                    v.sort()
                    if (str(v) not in b):
                        if (all_in(v) != False):
                            a.append(v)
                    b[str(v)] = True
        return a