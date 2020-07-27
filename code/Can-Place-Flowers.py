class Solution(object):

    def canPlaceFlowers(self, flowerbed, n):
        stack = []
        flowerCount = 0
        a = 0
        r = None
        while (len(flowerbed) > 0):
            if (a == 0):
                zeroCount = 1
                a = 1
            else:
                zeroCount = 0
            while ((len(flowerbed) > 0) and (flowerbed[0] == 0)):
                zeroCount += 1
                if (zeroCount == 3):
                    flowerCount += 1
                    zeroCount = 1
                r = flowerbed.pop(0)
            if (len(flowerbed) > 0):
                r = flowerbed.pop(0)
        print zeroCount
        if ((zeroCount == 2) and (r == 0)):
            flowerCount += 1
        return (flowerCount >= n)