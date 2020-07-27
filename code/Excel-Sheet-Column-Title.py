class Solution(object):

    def convertToTitle(self, n):
        a = list('abcdefghijklmnopqrstuvwxyz')
        val = ''

        def check(num):
            print num
            if ((num - 1) < 26):
                return a[(num - 1)]
            return (check((num / 26)) + a[(num % 26)])
        b = ''
        num = n
        while (((num - 1) // 26) > 0):
            b += a[((num - 1) % 26)]
            num = ((num - 1) // 26)
        b += a[((num - 1) % 26)]
        print b
        return b.upper()[::(-1)]
        print num