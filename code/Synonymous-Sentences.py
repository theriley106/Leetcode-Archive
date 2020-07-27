import itertools


class Solution(object):

    def generateSentences(self, synonyms, text):
        words = {}
        for val in synonyms:
            (e, y) = val
            if (e not in words):
                words[e] = []
            words[e].append(y)
            if (y not in words):
                words[y] = []
            words[y].append(e)
        for (k, v) in words.iteritems():
            words[k] = set(words[k])
        for (k, v) in words.iteritems():
            for y in list(words[k]):
                for w in words[y]:
                    words[k].add(w)
        newString = ''
        x = []
        for v in text.split(' '):
            if (v in words):
                x.append(list(words[v]))
            else:
                x.append([v])
        t = []
        for v in list(itertools.product(*x)):
            t.append(' '.join(v))
        return sorted(t)
        print newString
