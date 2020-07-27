class Solution(object):

    def busyStudent(self, startTime, endTime, queryTime):
        count = 0
        for i in xrange(len(startTime)):
            if ((endTime[i] >= queryTime) and (startTime[i] <= queryTime)):
                count += 1
        return count