class Solution(object):

    def buildArray(self, target, n):
        a = []
        ops = []
        currentMatchedPoint = 0
        for i in range(1, (n + 1)):
            a.append(i)
            ops.append('Push')
            if (a == target):
                break
            if (a[(-1)] == target[currentMatchedPoint]):
                currentMatchedPoint += 1
            else:
                a.pop((-1))
                ops.append('Pop')
        return ops