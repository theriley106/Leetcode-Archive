class Solution(object):

    def dailyTemperatures(self, T):
        T = list(T)
        unSolvedNumbers = []

        def add(index, val):
            for (i, unsolvedTemp) in enumerate(unSolvedNumbers):
                if (val <= unsolvedTemp['val']):
                    unSolvedNumbers.insert(i, {'index': index, 'val': val})
                    return
            unSolvedNumbers.append({'index': index, 'val': val})
        for (index, temperature) in enumerate(T):
            if (len(unSolvedNumbers) > 0):
                while (temperature > unSolvedNumbers[0]['val']):
                    T[unSolvedNumbers[0]['index']] = (
                        index - unSolvedNumbers[0]['index'])
                    unSolvedNumbers.pop(0)
                    if (len(unSolvedNumbers) == 0):
                        break
            add(index, temperature)
            T[index] = 0
        return T
