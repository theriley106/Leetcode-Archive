import string


class Solution(object):

    def generateTheString(self, n):
        if ((n % 2) == 0):
            stringVal = ''.join(['a' for i in range((n - 1))])
            return (stringVal + 'z')
        else:
            return ''.join(['a' for i in range(n)])
