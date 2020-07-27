class Solution(object):

    def checkIfExist(self, arr):
        for (i, val) in enumerate(arr):
            for (e, va) in enumerate(arr):
                if (i != e):
                    if (((va * 2) == val) or ((val * 2) == va)):
                        return True
        return False