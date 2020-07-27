MIN = ((2 ** 31) - 1)


class Solution(object):

    def reverse(self, x):
        neg = False
        a = list(str(x))[::(-1)]
        if ('-' in a):
            neg = True
            a.remove('-')
        f = int(''.join(a))
        if (f > MIN):
            return 0
        return (int(''.join(a)) * ((-1) if neg else 1))
