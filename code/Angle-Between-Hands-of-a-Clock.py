class Solution(object):

    def angleClock(self, hour, minutes):
        if (hour >= 12):
            hour = (hour - 12)
        oneMinuteDegrees = (360 / 60)
        minuteLocation = (minutes * oneMinuteDegrees)
        diffBetweenTicks = (minuteLocation / 360.0)
        hourAngle = (360 / 12)
        hourLocation = (hour * hourAngle)
        hourLocation += (hourAngle * diffBetweenTicks)
        print 'HOUR: {}'.format(hourLocation)
        print 'MINUTE: {}'.format(minuteLocation)
        return min(abs((minuteLocation - hourLocation)), (360 - abs((hourLocation - minuteLocation))))