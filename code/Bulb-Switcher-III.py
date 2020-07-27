class Solution(object):

    def __init__(self):
        self.bulbs = {}
        self.still_off = []

    def numTimesAllBlue(self, light):
        a = ['off' for i in range(len(light))]
        count = 0
        highestNum = 0
        highestBlue = 0
        for lightIndex in light:
            a[(lightIndex - 1)] = 'on'
            highestNum = max(highestNum, (lightIndex - 1))
            index = highestBlue
            while (((index < (len(a) - 1)) and (a[index] == 'on')) or (a[index] == 'blue')):
                a[index] = 'blue'
                if (index > highestBlue):
                    highestBlue = index
                index += 1
            if (index == (len(a) - 1)):
                a[index] = 'blue'
            if (a[highestNum] == 'blue'):
                count += 1
        return count