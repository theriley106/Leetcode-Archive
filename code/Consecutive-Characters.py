class Solution(object):

    def maxPower(self, s):
        a = list(s)
        maxCount = 1
        while (len(a) > 0):
            count = 1
            e = a.pop(0)
            while ((len(a) > 0) and (e == a[0])):
                count += 1
                a.pop(0)
            if (count > maxCount):
                maxCount = count
        return maxCount