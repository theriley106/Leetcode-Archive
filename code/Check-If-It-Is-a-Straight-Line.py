class Solution(object):

    def checkStraightLine(self, coordinates):

        def calc(x1, x2):
            return (float((x2[1] - x1[1])) / float((x2[0] - x1[0])))
        prevVal = None
        array = coordinates
        while (len(array) > 1):
            try:
                prev = calc(array.pop(0), array[0])
                if ((prev != prevVal) and (prevVal != None)):
                    return False
            except:
                return False
            prevVal = prev
        return True