class Solution(object):

    def addStrings(self, num1, num2):
        vals = {}
        for i in range(0, 11):
            vals[str(i)] = i
        tmpNum1 = list(num1)[::(-1)]
        tmpNum2 = list(num2)[::(-1)]
        total = 0
        multiply = 1
        while True:
            if ((len(tmpNum1) == 0) and (len(tmpNum2) == 0)):
                break
            num1 = 0
            num2 = 0
            if (len(tmpNum1) > 0):
                num1 = (vals[tmpNum1.pop(0)] * multiply)
            if (len(tmpNum2) > 0):
                num2 = (vals[tmpNum2.pop(0)] * multiply)
            total += (num1 + num2)
            multiply *= 10
        return str(total)