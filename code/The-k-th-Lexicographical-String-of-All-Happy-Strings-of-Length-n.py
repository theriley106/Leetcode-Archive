class Solution(object):

    def getHappyString(self, n, k):
        vals = ['a', 'b', 'c']
        self.count = 0
        self.found = ''

        def calc(val=''):
            if (len(val) == n):
                self.count += 1
                if (self.count == k):
                    self.found = val
                    print val
                return
            for v in vals:
                if ((len(val) == 0) or (v != val[(-1)])):
                    calc((val + v))
        calc()
        return self.found