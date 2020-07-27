class Solution(object):

    def reorderLogFiles(self, logs):
        a = []
        digits = []
        for l in logs:
            (v, deval, word) = l.partition(' ')
            try:
                print int(word[0])
                digitType = True
            except Exception as exp:
                print exp
                digitType = False
            if (digitType == True):
                digits.append(((v + ' ') + word))
            else:
                a.append({'v': v, 'word': word})
        h = []
        for val in sorted(a, key=(lambda k: k['word'])):
            h.append(((val['v'] + ' ') + val['word']))
        print h
        for val in digits:
            h.append(val)
        return h