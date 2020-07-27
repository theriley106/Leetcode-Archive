class Solution(object):

    def isOneBitCharacter(self, bits):
        while (len(bits) > 2):
            if (bits[0] == 0):
                bits.pop(0)
            else:
                bits.pop(0)
                bits.pop(0)
        x = list(set(bits))
        return ((len(bits) == 1) or ((len(x) == 1) and (x[0] == 0)))