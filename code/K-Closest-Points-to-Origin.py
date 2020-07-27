def calc_distance(a):
    x = (a[0] ** 2)
    y = (a[1] ** 2)
    return ((x + y) ** 0.5)


class Solution(object):

    def kClosest(self, points, K):
        a = []
        for val in points:
            distance = calc_distance(val)
            a.append({'points': val, 'distance': distance})
        a = [x['points'] for x in sorted(a, key=(lambda k: k['distance']))]
        return a[:K]
