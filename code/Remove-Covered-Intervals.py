class Solution(object):

    def removeCoveredIntervals(self, intervals):

        def should_delete(interval):
            for part in intervals:
                if (part != interval):
                    if ((interval[0] >= part[0]) and (interval[1] <= part[1])):
                        return True
            return False
        count = 0
        for part in intervals:
            if should_delete(part):
                count += 1
        return (len(intervals) - count)