class Solution(object):

    def readBinaryWatch(self, num):
        e = []
        for i in [8, 4, 2, 1]:
            e.append({'row': 'top', 'num': i})
        for i in [32, 16, 8, 4, 2, 1]:
            e.append({'row': 'lower', 'num': i})
        times = []
        for val in itertools.combinations(e, num):
            hours = 0
            mins = 0
            r = {'top': [], 'bottom': []}
            for v in val:
                if (v['row'] == 'top'):
                    hours += v['num']
                    r['top'].append(v['num'])
                else:
                    mins += v['num']
                    r['bottom'].append(v['num'])
            if ((mins < 60) and (hours < 12)):
                x = '{}:{}'.format(str(hours).zfill(1), str(mins).zfill(2))
                r['x'] = x
                print r
                times.append(x)
        return sorted(times)