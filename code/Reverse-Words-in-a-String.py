import re


class Solution(object):

    def reverseWords(self, s):
        return ' '.join(re.findall('S+', s)[::(-1)])
