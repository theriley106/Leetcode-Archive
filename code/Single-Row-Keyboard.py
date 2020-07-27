class Solution(object):

    def calculateTime(self, keyboard, word):
        total = 0
        index = 0
        for letters in word:
            newIndex = keyboard.index(letters)
            total += abs((index - newIndex))
            index = newIndex
        return total