class Solution(object):

    def insert(self, intervals, newInterval):

        def merge_interval(intervals):
            a = []
            prevVal = (-1)
            while (len(intervals) > 0):
                startInterval = intervals[0][0]
                endInterval = intervals[0][1]
                intervals.pop(0)
                while ((len(intervals) > 0) and (endInterval >= intervals[0][0])):
                    endInterval = max(intervals[0][1], endInterval)
                    intervals.pop(0)
                a.append([startInterval, endInterval])
            return a
        intervals.append(newInterval)
        intervals.sort(key=(lambda k: k[0]))
        print intervals
        return merge_interval(intervals)