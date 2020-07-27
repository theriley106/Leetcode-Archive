import datetime


class Solution(object):

    def dayOfTheWeek(self, day, month, year):
        a = ['monday', 'tuesday', 'wednesday',
             'thursday', 'friday', 'saturday', 'sunday']
        x = datetime.datetime.strptime(
            '{}-{}-{}'.format(day, month, year), '%d-%m-%Y')
        return a[x.weekday()].title()
