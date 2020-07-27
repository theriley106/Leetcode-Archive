class Solution(object):

    def read(self, buf, n):
        string = ''
        count = 0
        x = 'AY'
        temp = ([' '] * 4)
        while (x != 0):
            x = read4(temp)
            print x
            print temp
            for i in range(4):
                buf[(i + count)] = temp[i]
            count += x
            if (x < 4):
                break
        return min(n, count)