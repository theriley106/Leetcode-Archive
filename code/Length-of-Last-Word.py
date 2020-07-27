class Solution(object):

    def lengthOfLastWord(self, s):
        a = []
        listOfWords = s.split(' ')[::(-1)]
        for word in listOfWords:
            if (len(word) > 0):
                a.append(word)
        try:
            return len(a[0])
        except:
            return 0