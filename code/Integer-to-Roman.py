class Solution(object):

    def intToRoman(self, s):
        a = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        vals = sorted(a.keys())
        string = ''
        while (s > 0):
            temp = [(a[k], k) for k in vals if (k <= s)]
            (value, toSubtract) = temp[(-1)]
            s = (s - toSubtract)
            string += str(value)
        return string.replace('VIIII', 'IX').replace('IIII', 'IV').replace('DCCCC', 'CM').replace('LXXXX', 'XC').replace('XXXX', 'XL').replace('CCCC', 'CD')