class Solution(object):

    def stringShift(self, s, shift):

        def shiftz(string, direction, amount):
            string = list(string)
            if (direction == 0):
                for i in range(amount):
                    r = [string.pop(0)]
                    string = (string + r)
            else:
                for i in range(amount):
                    r = [string.pop((-1))]
                    string = (r + string)
            return ''.join(string)
        for val in shift:
            s = shiftz(s, val[0], val[1])
            print s
        return s