class Solution(object):

    def reverseWords(self, s):
        a = []
        r = ''.join(s).split(' ')
        e = r[::(-1)]
        index = 0
        for (i, val) in enumerate(e):
            for v in val:
                s[index] = v
                index += 1
            if (i != (len(e) - 1)):
                s[index] = ' '
            index += 1
        return a