class Solution(object):

    def lastStoneWeight(self, stones):
        stones.sort()

        def smash(rockList):
            if (len(rockList) == 1):
                return rockList
            a = rockList.pop((-1))
            b = rockList.pop((-1))
            if (a == b):
                pass
            rockList.append(abs((a - b)))
            rockList.sort()
            return smash(rockList)
        return smash(stones)[0]