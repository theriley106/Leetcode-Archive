class Solution(object):

    def hasAllCodes(self, s, k):
        r = set()
        for i in range(((len(s) - k) + 1)):
            r.add(s[i:(i + k)])
        self.combinations = []

        def get_all(left, prev=''):
            if (left == 0):
                self.combinations.append(prev)
                return
            get_all((left - 1), (prev + '1'))
            get_all((left - 1), (prev + '0'))
        get_all(k)
        for v in self.combinations:
            if (v not in r):
                return False
        return True