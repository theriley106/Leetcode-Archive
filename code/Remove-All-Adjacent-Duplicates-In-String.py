class Solution(object):

    def removeDuplicates(self, S):
        tempList = []
        S = list(S)
        for val in S:
            if (len(tempList) > 0):
                if (tempList[(-1)] == val):
                    tempList.pop((-1))
                else:
                    tempList.append(val)
            else:
                tempList.append(val)
        return ''.join(tempList)