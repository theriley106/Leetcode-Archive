class Solution(object):

    def merge(self, intervals):
        a = []
        intervals = sorted(intervals, key=(lambda x: x[0]))
        invervals2 = list(intervals)
        iVals = []
        if (len(intervals) > 0):
            maxVal = 0
            for val in intervals:
                if (val[(-1)] > maxVal):
                    maxVal = val[(-1)]
            a = [None for i in range((maxVal + 1))]
            for val in intervals:
                x = list(val)
                x[(-1)] = (x[(-1)] + 1)
                for i in range(*x):
                    if ((a[i] == 'X') or (a[i] == 'O')):
                        a[i] = 'O'
                    else:
                        a[i] = 'X'
            i = 0
            print a
        g = []

        def merge_all(listVal, num):
            toMerge = []
            for val in listVal:
                x = list(val)
                x[(-1)] = (x[(-1)] + 1)
                if (num in range(*x)):
                    toMerge.append(val)
            minVal = float('inf')
            maxVal = 0
            for val in toMerge:
                listVal.remove(val)
                if (val[0] < minVal):
                    minVal = val[0]
                if (val[1] > maxVal):
                    maxVal = val[1]
            listVal.append([minVal, maxVal])
            return listVal
        for (i, val) in enumerate(a):
            if (val == 'O'):
                intervals = merge_all(intervals, i)
        return intervals