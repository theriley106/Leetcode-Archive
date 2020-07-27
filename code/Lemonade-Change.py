class Solution(object):

    def lemonadeChange(self, bills):
        bank = []
        for transaction in bills:
            change = (transaction - 5)
            if (change == 0):
                pass
            else:
                if (change == 15):
                    if ((bank.count(10) > 0) or (bank.count(5) > 1)):
                        if (bank.count(10) > 0):
                            bank.remove(10)
                        else:
                            bank.remove(5)
                            bank.remove(5)
                        change = (change - 10)
                    else:
                        return False
                try:
                    bank.remove(5)
                except:
                    return False
            bank.append(transaction)
        return True