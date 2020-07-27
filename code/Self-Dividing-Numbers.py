class Solution(object):

    def selfDividingNumbers(self, left, right):
        dividingNum = []
        for i in range(left, (right + 1)):
            if ('0' not in str(i)):
                divide = True
                for num in list(str(i)):
                    if ((i % int(num)) != 0):
                        divide = False
                    else:
                        divide = True
                    if (divide == False):
                        break
                if (divide == True):
                    dividingNum.append(i)
        return dividingNum