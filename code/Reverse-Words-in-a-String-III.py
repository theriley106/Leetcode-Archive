class Solution(object):

    def reverseWords(self, s):
        a = []
        for word in s.split(' '):
            a.append(''.join(list(word)[::(-1)]))
        return ' '.join(a)