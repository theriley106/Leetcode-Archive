class Solution(object):

    def isAlienSorted(self, words, order):
        return (words == sorted(words, key=(lambda k: [order.index(x) for x in k])))