class Solution(object):

    def calPoints(self, ops):
        ongoingList = []
        while (len(ops) > 0):
            thisNum = None
            try:
                thisNum = int(ops[0])
                ops.pop(0)
            except:
                pass
            if (thisNum != None):
                ongoingList.append(int(thisNum))
            elif (len(ops) > 0):
                val = ops.pop(0)
                if (val == 'D'):
                    ongoingList.append((ongoingList[(-1)] * 2))
                elif (val == 'C'):
                    ongoingList.pop((-1))
                else:
                    ongoingList.append((ongoingList[(-1)] + ongoingList[(-2)]))
        return sum(ongoingList)