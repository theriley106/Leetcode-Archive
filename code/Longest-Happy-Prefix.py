class Solution(object):

    def longestPrefix(self, s):
        final = ''
        maxFinalSize = 0
        a = []
        for i in xrange(1, len(s)):
            try:
                string = s[:(len(s) - i)]
                if (string == s[(len(string) * (-1)):]):
                    return string
                    final = string
                    a.append(string)
            except:
                pass
        if (len(a) == 0):
            return ''
        return sorted(a, key=(lambda k: len(k)))[(-1)]
        return final