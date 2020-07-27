class Solution(object):

    def nextGreaterElements(self, nums):
        tmpArray = (nums * 3)
        start = len(nums)
        valList = []
        for (e, val) in enumerate(nums):
            maxVal = (-1)
            found = False
            for i in range(e, (start + e)):
                if (found == True):
                    if (tmpArray[(start + i)] > val):
                        maxVal = tmpArray[(start + i)]
                        break
                if (tmpArray[(start + i)] == val):
                    found = True
            valList.append(maxVal)
        return valList