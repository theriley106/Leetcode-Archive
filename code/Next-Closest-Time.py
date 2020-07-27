import re


class Solution(object):

    def nextClosestTime(self, time):

        def diff_time(string1, string2):
            if (string1 == string2):
                return float('inf')
            if ((int(string2[:2]) >= 24) or (int(string2[2:]) >= 60)):
                return float('inf')
            r = (int(string2) - int(string1))
            if (int(string1) > int(string2)):
                return (2400 - (int(string1) - int(string2)))
            return r
        digits = re.findall('d', time)
        closest = float('inf')
        newVal = ''.join(digits)
        for val in list(itertools.permutations((digits * 4), 4)):
            time2 = '{}{}{}{}'.format(val[0], val[1], val[2], val[3])
            e = diff_time(time.replace(':', ''), time2)
            if (e < closest):
                closest = e
                newVal = time2
        return ((newVal[:2] + ':') + newVal[2:])
