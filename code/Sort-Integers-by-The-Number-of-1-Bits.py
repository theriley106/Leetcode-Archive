class Solution(object):

    def sortByBits(self, arr):

        def get_val(num):
            return str(bin(num))[2:].count('1')
        db = {}
        for val in arr:
            values = get_val(val)
            if (values not in db):
                db[values] = []
            db[values].append(val)
        a = []
        nums = sorted(db.keys())
        for key in nums:
            for val in sorted(db[key]):
                a.append(val)
        return a