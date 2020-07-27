class Solution(object):

    def validWordSquare(self, words):
        maxLength = max(([len(x) for x in words] + [len(words)]))
        newWords = [['*' for i in range(maxLength)] for i in range(maxLength)]
        for (i, val) in enumerate(words):
            words[i] = list(words[i])
            while (len(words[i]) < maxLength):
                words[i].append('*')
            for (e, val2) in enumerate(words[i]):
                newWords[e][i] = val2
        while (len(words) < maxLength):
            words.append(['*' for i in range(maxLength)])
        for val in words:
            print val
        print 'AYY'
        for (i, val) in enumerate(newWords):
            for (e, val2) in enumerate(val):
                if (val2 != words[i][e]):
                    return False
            print val
        return True