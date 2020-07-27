class Solution(object):

    def canAttendMeetings(self, intervals):
        newList = sorted(intervals, key=(lambda k: k[0]))
        for i in range((len(newList) - 1)):
            if (newList[i][1] > newList[(i + 1)][0]):
                return False
        return True