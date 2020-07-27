from datetime import datetime


class Solution(object):

    def daysBetweenDates(self, date1, date2):
        x = (datetime.strptime(date1, '%Y-%m-%d') -
             datetime.strptime(date2, '%Y-%m-%d'))
        return abs(x.days)
