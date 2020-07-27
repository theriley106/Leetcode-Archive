class Solution(object):

    def compare(num1, num2, direction):
        if (direction > 0):
            return (num1 > num2)
        return (num1 < num2)

    def dfs(xIndex, yIndex, targetX, targetY, direction=1):
        if ((xIndex == targetX) and (yIndex == targetY)):
            return 0
        incrementX = compare(xIndex, targetX, direction)
        incrementY = compare(yIndex, targetY, direction)
        count = 0
        if (incrementX and incrementY):
            count = compare((xIndex + direction), (yIndex +
                                                   direction), targetX, targetY, direction)
        elif incrementX:
            count = compare((xIndex + direction), yIndex,
                            targetX, targetY, direction)
        else:
            count = compare(xIndex, (yIndex + direction),
                            targetX, targetY, direction)
        return (1 + count)

    def calc(self, pt1, pt2):
        a = (pt2[1] - pt1[1])
        b = (pt2[0] - pt1[0])
        print [a, b]
        return max([abs(a), abs(b)])
        return ((a * a) + (b * b))

    def minTimeToVisitAllPoints(self, points):
        compare = points.pop(0)
        total = 0
        while (len(points) > 0):
            print 'Comparing {} to {}'.format(compare, points[0])
            x = self.calc(compare, points[0])
            print x
            total += x
            compare = points.pop(0)
        return total
