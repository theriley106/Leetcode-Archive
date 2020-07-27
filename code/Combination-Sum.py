import itertools


class Solution(object):

    def combinationSum(self, candidates, target):
        a = set()
        allVals = []

        def check_if_combine(number, vals=[]):
            if (number == 0):
                r = sorted(vals)
                if (r not in allVals):
                    allVals.append(r)
            if (number < 0):
                return
            for val in [x for x in candidates if (x <= number)]:
                check_if_combine((number - val), (vals + [val]))
        check_if_combine(target)
        return allVals
