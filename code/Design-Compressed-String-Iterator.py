import re


class StringIterator(object, ):

    def __init__(self, compressedString):
        self.a = []
        x = re.findall('D+', compressedString)
        print x
        b = re.findall('d+', compressedString)
        print b
        for i in range(len(x)):
            self.a.append(((x[i] + '&') + b[i]))

    def next(self):
        val = ' '
        try:
            (v, num) = self.a[0].split('&')
            if (int(num) == 1):
                self.a.pop(0)
            else:
                self.a[0] = (v + '&{}'.format((int(num) - 1)))
            return v
        except Exception as exp:
            print exp
            return ' '

    def hasNext(self):
        return (len(self.a) > 0)
