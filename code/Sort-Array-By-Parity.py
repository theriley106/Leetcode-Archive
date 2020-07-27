class Solution(object):

    def sortArrayByParity(self, A):
        a = []
        b = []
        for val in A:
            if ((val % 2) == 0):
                b.append(val)
            else:
                a.append(val)
        return (b + a)