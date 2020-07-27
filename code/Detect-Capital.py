class Solution(object):

    def detectCapitalUse(self, word):
        return ((word == word.title()) or (word == word.upper()) or (word == word.lower()))