class Solution(object):

    def stringMatching(self, words):
        a = []
        for (i, word) in enumerate(words):
            for (e, word2) in enumerate(words):
                if (i != e):
                    if (word in word2):
                        a.append(word)
        return list(set(a))