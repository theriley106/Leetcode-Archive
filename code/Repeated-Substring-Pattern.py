class Solution(object):

    def repeatedSubstringPattern(self, s):
        i = 1
        while ((i > 0) and (i <= (len(s) / 2))):
            if (((len(s[:i]) * s.count(s[:i])) == len(s)) and (s[:i] != s)):
                return True
            i += 1
        return False