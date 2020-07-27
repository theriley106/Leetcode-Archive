class Solution(object):

    def dayOfYear(self, date):
        (year, month, day) = [int(x) for x in date.split('-')]
        leap = False
        if ((year % 4) == 0):
            if ((year % 100) == 0):
                if ((year % 400) == 0):
                    leap = True
            else:
                leap = True
        thirtyOneDays = [1, 3, 5, 7, 8, 10, 12]
        thirtyDays = [4, 6, 9, 11]
        total = day
        print leap
        for i in range(1, month):
            if (i in thirtyOneDays):
                total += 31
            elif (i in thirtyDays):
                total += 30
            else:
                total += 28
            if ((leap == True) and (i == 2)):
                total += 1
        return total