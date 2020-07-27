class Solution(object):

    def shortestDistance(self, words, word1, word2):
        db = {word1: [], word2: []}
        for (i, v) in enumerate(words):
            if (v == word1):
                db[v].append(i)
            if (v == word2):
                db[v].append(i)
        print db
        distance = float('inf')
        for i in db[word1]:
            for e in db[word2]:
                distance = min(distance, abs((i - e)))
        return distance