import re


class Solution(object):

    def maskPII(self, S):
        if ('@' in S):
            (name, email) = S.split('@')
            name = name.lower()
            first = name[0]
            last = name[(-1)]
            name = ''.join((([first] + ['*' for i in range(5)]) + [last]))
            return '{}@{}'.format(name, email.lower())
        else:
            S = S.replace('(', '').replace(')', '').replace(' ', '')
            e = list(''.join(re.findall('d+', S)))
            homeNum = e[(-10):]
            for i in range(10):
                e.pop((-1))
            if (len(e) > 0):
                t = ''.join(['*' for i in range(len(e))])
                countryNum = (('+' + ''.join(t)) + '-')
            else:
                countryNum = ''
            r = list(homeNum)
            tempNum = ''
            for i in range(3):
                tempNum += '*'
                r.pop(0)
            tempNum += '-'
            for i in range(3):
                tempNum += '*'
                r.pop(0)
            tempNum += '-'
            tempNum += ''.join(r)
            return '{}{}'.format(countryNum, tempNum)
