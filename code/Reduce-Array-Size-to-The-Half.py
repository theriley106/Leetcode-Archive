class Solution(object):

    def minSetSize(self, arr):
        db = {}
        for val in arr:
            if (val not in db):
                db[val] = 0
            db[val] += 1
        fullSize = len(arr)
        a = []
        for (key, val) in db.iteritems():
            a.append([key, val])
        a.sort(key=(lambda k: k[1]), reverse=True)
        targetSize = (fullSize / 2)
        count = 0
        for val in a:
            fullSize = (fullSize - val[1])
            count += 1
            if (fullSize <= targetSize):
                return count
        print a