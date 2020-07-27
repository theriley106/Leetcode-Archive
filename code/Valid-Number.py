import re


class Solution(object):

    def isNumber(self, s):
        try:
            r = float(s.strip())
            return True
        except Exception as exp:
            print exp
            return False
