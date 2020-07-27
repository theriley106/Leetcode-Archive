import math


class Solution(object):

    def removePalindromeSub(self, s):

        def is_palindrome(string):
            string = list(string)
            a = string.pop(0)
            b = string.pop((-1))
            while ((a == b) and (len(string) > 0)):
                a = string.pop(0)
                try:
                    b = string.pop((-1))
                except:
                    return True
            return (a == b)
        if (len(s) == 0):
            return 0
        if is_palindrome(s):
            return 1
        return 2
        a = {}
        for val in s:
            if (val not in a):
                a[val] = 0
            a[val] += 1
        if (len(set(a.values())) < 2):
            return 1
        else:
            return 2
        print a
