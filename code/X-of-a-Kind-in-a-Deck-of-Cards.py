class Solution(object):

    def hasGroupsSizeX(self, deck):
        v = {}
        for val in deck:
            if (val not in v):
                v[val] = 0
            v[val] += 1
        for e in range(2, (min(v.values()) + 1)):
            cont = True
            for (i, val) in v.iteritems():
                if ((val % e) != 0):
                    cont = False
                    break
            if (cont == True):
                return True
        return False