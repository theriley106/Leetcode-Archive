class Solution(object):

    def depthSum(self, nestedList):
        db = {}

        def get(listVal, depth):
            valz = 0
            if (depth not in db):
                db[depth] = []
            if (type(listVal) == list):
                for val in listVal:
                    get(val, (depth + 1))
            elif listVal.isInteger():
                db[depth].append(listVal.getInteger())
            else:
                for val in listVal.getList():
                    get(val, (depth + 1))
        print get(nestedList, 0)
        print db
        start = (max(db.keys()) + 1)
        newDB = {}
        sumVal = 0
        for (k, v) in db.iteritems():
            sumVal += (sum(v) * k)
        return sumVal