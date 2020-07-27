import re


class Solution(object):

    def reformatDate(self, date):
        a = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        monthIndex = (a.index(str(date).partition(' ')
                              [2].partition(' ')[0]) + 1)
        (day, year) = re.findall('d+', date)
        return '{}-{}-{}'.format(year, zfill(monthIndex, 2), zfill(int(day), 2))
