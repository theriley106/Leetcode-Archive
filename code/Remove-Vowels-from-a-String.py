class Solution(object):

    def removeVowels(self, S):
        vowels = 'aeiou'
        for val in vowels:
            S = S.replace(val, '')
        return S