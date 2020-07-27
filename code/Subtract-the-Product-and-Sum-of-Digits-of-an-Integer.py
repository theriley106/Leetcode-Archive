class Solution(object):

    def subtractProductAndSum(self, n):
        a = [int(x) for x in str(n)]
        r = 1
        for val in a:
            r *= val
        return (r - sum(a))