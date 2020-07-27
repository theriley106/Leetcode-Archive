class Solution(object):

    def minNumberOfFrogs(self, croakOfFrogs):
        db = {}
        numCroaks = (len(croakOfFrogs) / 5)
        for v in 'croak':
            db[v] = numCroaks

        def is_valid():
            return ([db[x] for x in 'croak'] == sorted([db[x] for x in 'croak']))
        maxK = 0
        for letter in croakOfFrogs:
            db[letter] -= 1
            found = False
            if (not is_valid()):
                return (-1)
            x = (db['k'] - db['c'])
            if (x > maxK):
                maxK = x
        if ((max(db.values()) > 0) or ((-1) in db.values())):
            return (-1)
        return maxK