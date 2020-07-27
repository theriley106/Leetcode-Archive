class Solution(object):

    def reverseVowels(self, s):
        vowels = ['a', 'e', 'i', 'o', 'u']
        non_vowels = []
        vowel_letters = []
        for letter in s:
            if (letter.lower() in vowels):
                vowel_letters.append(letter)
                non_vowels.append(None)
            else:
                non_vowels.append(letter)
        for (i, letter) in enumerate(non_vowels):
            if (letter == None):
                non_vowels[i] = vowel_letters.pop((-1))
        return ''.join(non_vowels)