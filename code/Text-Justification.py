class Solution(object):

    def fullJustify(self, words, maxWidth):
        e = []
        while (len(words) > 0):
            currentLine = ''
            wordCount = 0
            word_list = []
            while ((len(words) > 0) and ((len(currentLine) == 0) or (len((currentLine + ' {}'.format(words[0]))) <= maxWidth))):
                print 'TOP LOOP'
                r = words.pop(0)
                word_list.append(r)
                if (len(currentLine) == 0):
                    currentLine += '{}'.format(r)
                else:
                    currentLine += ' {}'.format(r)
                wordCount += len(r)
            wordDistance = (maxWidth - wordCount)
            if (len(words) != 0):
                while ((wordDistance > 0) and ((len(word_list) - 1) > 0)):
                    for i in range((len(word_list) - 1)):
                        if (wordDistance > 0):
                            word_list[i] = (word_list[i] + ' ')
                            wordDistance = (wordDistance - 1)
                currentLine = ''.join(word_list)
            while (len(currentLine) < maxWidth):
                currentLine += ' '
            e.append(currentLine)
        return e