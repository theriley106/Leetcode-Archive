class Solution(object):

    def canConstruct(self, ransomNote, magazine):
        magazine = list(magazine)
        ransomNote = list(ransomNote)
        if (len(ransomNote) == 0):
            return True
        while (len(magazine) > 0):
            letter = magazine.pop(0)
            if (letter in ransomNote):
                ransomNote.remove(letter)
            if (len(ransomNote) == 0):
                return True
        return False