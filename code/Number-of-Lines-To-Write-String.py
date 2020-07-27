import string


class Solution(object):

    def numberOfLines(self, widths, S):

        def roundUp(num):
            return (int(((num * 0.01) + 1)) * 100)
        alphabet_vals = string.ascii_lowercase
        i = 0
        tempAddVal = 0
        for val in S:
            tempVal = widths[alphabet_vals.index(val)]
            if ((((i + tempVal) / 100) > tempAddVal) and (((i + tempVal) % 100) != 0)):
                i = roundUp(i)
            i += tempVal
            tempAddVal = (i / 100)
        a = [(i / 100), (i % 100)]
        if (a[1] > 0):
            a[0] = (a[0] + 1)
        return a
