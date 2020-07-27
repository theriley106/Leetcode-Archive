class Solution(object):

    def arrangeWords(self, text):
        r = list(
            ' '.join(sorted([x.lower() for x in text.split(' ')], key=(lambda k: len(k)))))
        if (len(r) > 0):
            r[0] = r[0].upper()
        return ''.join(r)
