class Solution(object):

    def plusOne(self, digits):
        newNum = (int(''.join([str(d) for d in digits])) + 1)
        return [int(t) for t in str(newNum)]