class Solution(object):

    def canReach(self, arr, start):

        def check(index):
            return ((index > (-1)) and (index < len(arr)))
        db = {}

        def rec(index, prev=set(), vals=set()):
            print 'vals', vals
            print 'prev', prev
            if (0 in vals):
                print 'AYY'
                return True
            if (check(index) == False):
                return False
            if (index in prev):
                return False
            prev.add(index)
            vals.add(arr[index])
            db[index] = (rec((index + arr[index]), prev, vals)
                         or rec((index - arr[index]), prev, vals))
            return db[index]
        rec(start)
        return (True in db.values())
