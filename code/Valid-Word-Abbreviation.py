import re


class Solution(object):

    def validWordAbbreviation(self, word, abbr):

        def is_int(string):
            try:
                int(string)
                return True
            except:
                return False
        word = ' {} '.format(word)
        abbrList = list(abbr)
        newWord = ''
        while (len(abbrList) > 0):
            intVal = ''
            while ((len(abbrList) > 0) and is_int(abbrList[0])):
                intVal += abbrList.pop(0)
            if (len(intVal) > 0):
                if (intVal[0] == '0'):
                    return ''
                if (int(intVal) > len(word)):
                    return ''
                for i in range(int(intVal)):
                    newWord += '.'
            if (len(abbrList) > 0):
                newWord += abbrList.pop(0)
        newWord = 's{}s'.format(newWord)
        print word
        print newWord
        print re.findall(newWord, word)
        return (len(re.findall(newWord, word)) > 0)
