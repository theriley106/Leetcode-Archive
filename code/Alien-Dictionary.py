class Solution(object):

    def __init__(self):
        self.letterDB = {}
        self.alphabet = []
        self.allLetters = set()

    def create_db(self, words):
        orderVals = []
        nextVals = []
        for word in words:
            if (len(word) == 0):
                pass
            else:
                currentLetter = word.pop(0)
                self.allLetters.add(currentLetter)
                if ((len(orderVals) == 0) or (currentLetter != orderVals[(-1)])):
                    orderVals.append(currentLetter)
                    nextVals.append([word])
                else:
                    nextVals[(-1)].append(word)
        prevVals = []
        for i in range(len(orderVals)):
            if (orderVals[i] not in self.letterDB):
                self.letterDB[orderVals[i]] = set()
            for val in prevVals:
                self.letterDB[orderVals[i]].add(val)
            prevVals.append(orderVals[i])
        for wordList in nextVals:
            self.create_db(wordList)

    def create_alphabet(self):
        while (len(self.letterDB) > 0):
            for (key, val) in self.letterDB.iteritems():
                if (len(val) == 0):
                    self.alphabet.append(key)
                    break
            del self.letterDB[key]
            for (k, v) in self.letterDB.iteritems():
                if (key in v):
                    v.remove(key)

    def alienOrder(self, words):
        words = [list(x) for x in words]
        self.create_db(words)
        self.create_alphabet()
        if (len(self.alphabet) != len(self.allLetters)):
            return ''
        return ''.join(self.alphabet)