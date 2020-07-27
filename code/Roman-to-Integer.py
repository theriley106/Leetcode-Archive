class Solution(object):

    def romanToInt(self, s):
        a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s = s.replace('IV', 'IIII').replace('IX', 'IIIIIIIII').replace(
            'XL', 'XXXX').replace('XC', 'XXXXXXXXX')
        s = s.replace('CD', 'CCCC').replace('CM', 'CCCCCCCCC')
        count = 0
        for val in s:
            count += a[val]
        return count
