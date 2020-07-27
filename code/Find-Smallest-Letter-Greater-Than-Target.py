import string


class Solution(object):

    def nextGreatestLetter(self, letterList, target):
        self.letters = list((string.ascii_lowercase * 3))
        self.target = target
        self.letterIndex = self.letters.index(target)

        def calc_distance(letter):
            x = self.letters.index(letter)
            self.letters[x] = None
            z = self.letters.index(letter)
            self.letters[x] = letter
            self.letters[self.letterIndex] = target
            print (x - self.letterIndex)
            print (z - self.letterIndex)
            if ((x - self.letterIndex) < 0):
                x = 99999
            else:
                x = (x - self.letterIndex)
            if ((z - self.letterIndex) < 0):
                z = 99999
            else:
                z = (z - self.letterIndex)
            return min(x, z)
        for v in sorted(letterList, key=(lambda k: calc_distance(k))):
            if (v != target):
                return v
