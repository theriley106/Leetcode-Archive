class Solution(object):

    def convert(self, s, numRows):
        finalZig = [[] for i in range(numRows)]
        s = list(s)
        o = ''
        y = 0
        while (len(s) > 0):
            y += 1
            print y
            for i in range(numRows):
                try:
                    finalZig[i].append(s.pop(0))
                except Exception as exp:
                    break
            index = (numRows - 2)
            while (index > 0):
                for i in range(numRows):
                    if (i != index):
                        finalZig[i].append('')
                    else:
                        try:
                            finalZig[i].append(s.pop(0))
                        except:
                            break
                index = (index - 1)
        o = ''
        for v in finalZig:
            o += ''.join(v)
        return o