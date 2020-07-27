class Solution(object):

    def toHexspeak(self, num):
        validIf = {'A', 'B', 'C', 'D', 'E', 'F', 'I', 'O'}
        print num
        newString = str(hex(int(num)))[2:].upper().replace(
            '0', 'O').replace('1', 'I')
        print newString
        for val in newString:
            if (str(val) not in validIf):
                return 'ERROR'
        return newString
