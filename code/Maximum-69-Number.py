class Solution(object):

    def maximum69Number(self, num):
        maxNum = int(num)
        a = str(num)
        db = {'9': '6', '6': '9'}
        for i in xrange(len(a)):
            maxNum = max(int(((a[:i] + db[a[i]]) + a[(i + 1):])), maxNum)
        return maxNum