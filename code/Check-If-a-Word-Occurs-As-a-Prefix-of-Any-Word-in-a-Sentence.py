class Solution(object):

    def isPrefixOfWord(self, sentence, searchWord):
        for (i, val) in enumerate(sentence.split(' ')):
            if (val[:len(searchWord)] == searchWord):
                return (i + 1)
        return (-1)