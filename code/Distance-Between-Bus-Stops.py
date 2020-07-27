class Solution(object):

    def distanceBetweenBusStops(self, distance, start, destination):
        r = sum(distance)
        count = 0
        for i in range(min(start, destination), max(start, destination)):
            count += distance[i]
        print count
        print r
        return min(count, (r - count))