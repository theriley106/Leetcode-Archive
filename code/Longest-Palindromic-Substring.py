class Solution(object):

    def longestPalindrome(self, s):

        def is_palidrome(string):
            return (string == string[::(-1)])
        lVal = ''
        maxVal = 0
        for i in range(len(s)):
            for e in range(maxVal, ((len(s) - i) + 1)):
                if is_palidrome(s[i:(i + e)]):
                    print s[i:(i + e)]
                    if (len(s[i:(i + e)]) > maxVal):
                        lVal = ''.join(s[i:(i + e)])
                        maxVal = len(s[i:(i + e)])
        return lVal