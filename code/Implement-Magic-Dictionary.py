class MagicDictionary(object, ):

    def __init__(self):
        self.words = []

    def buildDict(self, dictVal):
        for val in dictVal:
            self.words.append(val)

    def search(self, word):
        for val in self.words:
            count = 0
            x = list(val)
            if (len(word) == len(x)):
                i = 0
                c = 0
                found = False
                while (((x[i] == word[i]) or (c < 1)) and (i < len(x))):
                    if (x[i] != word[i]):
                        c += 1
                    i += 1
                    if (i >= len(x)):
                        if (c == 1):
                            found = True
                        break
                print '{} - {}'.format(x[(i - 1)], word[(i - 1)])
                if found:
                    return True
        return False