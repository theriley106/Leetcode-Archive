import re


class WordDictionary(object, ):

    def __init__(self):
        self.searches = {}
        self.words = []

    def addWord(self, word):
        self.searches = {}
        self.words.append(word)

    def search(self, word):
        if (word not in self.searches):
            j = re.findall(word.replace('.', 'S'), ' '.join(self.words))
            self.searches[word] = (
                len((set(self.words) - set(j))) != len(set(self.words)))
        return self.searches[word]
