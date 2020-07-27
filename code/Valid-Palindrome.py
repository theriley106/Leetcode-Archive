import re


class Solution(object):

    def isPalindrome(self, s):
        var = ''.join(re.findall('w+', str(s))).lower()
        if (var == var[::(-1)]):
            return True
        else:
            return False
