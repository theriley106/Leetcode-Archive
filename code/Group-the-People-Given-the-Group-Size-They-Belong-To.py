class Solution(object):

    def groupThePeople(self, groupSizes):
        db = {}
        for (i, val) in enumerate(groupSizes):
            if (val not in db):
                db[val] = []
            db[val].append(i)
        print db
        a = []
        for (k, v) in db.iteritems():
            while (len(v) > 0):
                info = []
                for i in range(k):
                    info.append(v.pop(0))
                a.append(info)
        return a