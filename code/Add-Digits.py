class Solution(object):

    def addDigits(self, num):
        while (len(str(num)) > 1):
            var = list(str(num))
            a = 0
            for inte in var:
                a += int(inte)
            num = a
        return num