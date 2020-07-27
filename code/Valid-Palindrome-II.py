def isValid(s):
    try:
        while (s[(-1)] == s[0]):
            s.pop((-1))
            s.pop(0)
    except:
        pass
    return (len(s) == 0)


class Solution:

    def validPalindrome(self, s):
        s = list(s)
        if (s[::(-1)] == s):
            return True
        while (s[(-1)] == s[0]):
            s.pop((-1))
            s.pop(0)
        if (len(s) > 1):
            return (isValid(list(s)[1:]) or isValid(list(s)[:(-1)]))
        return True
