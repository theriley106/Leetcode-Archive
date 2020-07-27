import re


class Solution(object):

    def checkRecord(self, s):
        for var in re.findall('L+', str(s)):
            if (len(var) > 2):
                return False
        if (len(re.findall('A', str(s))) > 1):
            return False
        else:
            return True
