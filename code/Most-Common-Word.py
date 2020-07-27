import string


class Solution(object):

    def mostCommonWord(self, paragraph, banned):
        listOfWords = banned
        allWords = []
        for word in paragraph.split(' '):
            for letter in string.punctuation:
                word = word.replace(letter, '')
            word = word.lower()
            if (word not in listOfWords):
                allWords.append(word)
        highWordCount = 0
        highWord = None
        for word in list(set(allWords)):
            wordCount = allWords.count(word)
            if (wordCount > highWordCount):
                highWordCount = wordCount
                highWord = word
        return highWord
