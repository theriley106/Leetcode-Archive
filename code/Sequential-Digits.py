class Solution(object):

    def sequentialDigits(self, low, high):
        setVal = set()

        def get_all(currNum, minVal, maxVal):
            if (int(currNum[(-1)]) == 0):
                return
            if (int(currNum) > maxVal):
                return
            if (int(currNum) >= minVal):
                setVal.add(int(currNum))
            get_all(
                (str(currNum) + '{}'.format((int(currNum[(-1)]) + 1))), minVal, maxVal)
        for i in range(1, 10):
            get_all(str(i), low, high)
        print setVal
        return sorted(list(setVal))
