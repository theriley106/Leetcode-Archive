class Solution(object):

    def countLetters(self, S):

        def oneLetter(val):
            return (len(set(val)) == 1)
        count = 0
        s = S
        for i in xrange(len(s)):
            index = i
            while (((index + 1) <= len(s)) and (s[i] == s[i:(index + 1)][(-1)])):
                count += 1
                index += 1
        return count