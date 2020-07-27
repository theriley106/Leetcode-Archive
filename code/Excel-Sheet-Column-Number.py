import string


class Solution(object):

    def titleToNumber(self, s):
        a = string.ascii_uppercase
        totalNumber = 0
        for (i, letter) in enumerate(s[::(-1)]):
            totalNumber += ((a.index(letter) + 1) * (26 ** i))
        return totalNumber
