DIGITS = {1: [], 2: list('abc'), 3: list('def'), 4: list('ghi'), 5: list(
    'jkl'), 6: list('mno'), 7: list('pqrs'), 8: list('tuv'), 9: list('wxyz'), 0: []}


class Solution(object):

    def __init__(self):
        self.vals = []

    def get_all(self, digitsLeft, prev=''):
        if (len(digitsLeft) == 0):
            self.vals.append(prev)
            return
        a = []
        for val in DIGITS.get(int(digitsLeft[0]), []):
            self.get_all(digitsLeft[1:], (prev + val))
        return a

    def letterCombinations(self, digits):
        vals = []
        self.get_all(digits)
        return [x for x in self.vals if (len(x) > 0)]
