class Solution(object):

    def expand(self, S):
        self.allVals = []

        def get(string, results=''):
            if (len(string) == 0):
                self.allVals.append(results)
                return
            if (string[0] == '{'):
                tempString = ''
                i = 1
                while (string[i] != '}'):
                    tempString += string[i]
                    i += 1
                for letter in tempString.split(','):
                    get(string[(i + 1):], (results + letter))
            else:
                get(string[1:], (results + string[0]))
        get(S)
        return sorted(self.allVals)