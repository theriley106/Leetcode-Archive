class Solution(object):

    def minMeetingRooms(self, intervals):
        newListVals = sorted(intervals, key=(lambda k: k[0]))

        def check(newList):
            overLap = []
            for i in range((len(newList) - 1)):
                if (newList[i][1] > newList[(i + 1)][0]):
                    overLap.append([newList[(i + 1)][0], newList[i][1]])
            return overLap
        count = 0
        while (len(newListVals) > 0):
            count += 1
            newListVals = check(newListVals)
        return count