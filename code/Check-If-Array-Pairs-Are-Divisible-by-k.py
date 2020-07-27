class Solution(object):

    def canArrange(self, arr, k):
        db = {}
        pairs = []
        arr = [(x % k) for x in arr]
        for (i, val) in enumerate(arr):
            if ((k - val) in db):
                pairs.append([arr[i], (k - val)])
                db[(k - val)] -= 1
            else:
                if (val not in db):
                    db[val] = 0
                db[val] += 1
            if (db.get((k - val)) == 0):
                del db[(k - val)]
            if (db.get(val) == 0):
                del db[val]
        count = len(pairs)
        if ((db.get(0, 0) % 2) == 0):
            count += (db.get(0, 0) / 2)
        return (count == (len(arr) / 2))