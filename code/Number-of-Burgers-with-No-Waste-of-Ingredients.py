class Solution(object):

    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        if ((tomatoSlices % 2) != 0):
            return []
        if ((tomatoSlices == 0) and (cheeseSlices == 0)):
            return [0, 0]
        numberOfSmallBurgers = (tomatoSlices / 2)
        numberOfLargeBurgers = (numberOfSmallBurgers - cheeseSlices)
        a = numberOfLargeBurgers
        b = (numberOfSmallBurgers - (numberOfLargeBurgers * 2))
        if ((a < 0) or (b < 0)):
            return []
        return [a, b]
        print a
        print self.a
        return self.a