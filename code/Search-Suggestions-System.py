class Solution(object):

    def suggestedProducts(self, products, searchWord):
        self.vals = []

        def search(term, index, wordList):
            e = []
            if (index >= len(term)):
                return
            for v in wordList:
                if (v[:(index + 1)] == term[:(index + 1)]):
                    e.append(v)
            self.vals.append(sorted(e)[:3])
            search(term, (index + 1), e)
        search(searchWord, 0, products)
        return self.vals