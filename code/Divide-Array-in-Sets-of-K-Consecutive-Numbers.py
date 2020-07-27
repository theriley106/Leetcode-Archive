class Solution(object):

    def isPossibleDivide(self, nums, k):
        db = {}
        for val in nums:
            if (val not in db):
                db[val] = 0
            db[val] += 1

        def get_lowest(prevNumber=None):
            x = None
            if (prevNumber == None):
                x = sorted(db.keys())[0]
            elif ((prevNumber + 1) not in db):
                return None
            else:
                x = (prevNumber + 1)
            if (x == None):
                return None
            db[x] -= 1
            if (db[x] == 0):
                del db[x]
            return x
        print db
        allVals = []
        while (len(db) > 0):
            e = []
            for i in range(k):
                if (i == 0):
                    prevNumber = None
                r = get_lowest(prevNumber)
                if (r == None):
                    return False
                prevNumber = r
                e.append(r)
            allVals.append(e)
        print allVals
        for v in allVals:
            if (len(v) != k):
                return False
        return True
        return