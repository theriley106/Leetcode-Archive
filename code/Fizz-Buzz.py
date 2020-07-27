class Solution(object):

    def fizzBuzz(self, n):
        all_vals = []
        for i in range(1, (n + 1)):
            stringVal = ''
            if ((i % 3) == 0):
                stringVal += 'Fizz'
                if ((i % 5) == 0):
                    stringVal += 'Buzz'
            elif ((i % 5) == 0):
                stringVal += 'Buzz'
            else:
                stringVal += str(i)
            all_vals.append(stringVal)
        return all_vals