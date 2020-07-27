class Solution(object):

    def indexPairs(self, text, words):
        a = []
        for word in words:
            e = 0
            u = 0
            prev = (-1)
            temp = str(text)
            m = 0
            while (u == 0):
                try:
                    print 'FINDING {} IN {}'.format(word, temp)
                    e = temp.index(word)
                    temp = temp[1:]
                    o = [(e + m), (((e + len(word)) + m) - 1)]
                    if (o in a):
                        pass
                    else:
                        a.append([(e + m), (((e + len(word)) + m) - 1)])
                    e = ((e + len(word)) - 1)
                    m += 1
                except Exception as exp:
                    print exp
                    u = 1
        return sorted(a)