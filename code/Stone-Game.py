class Solution(object):

    def turn(self, stones, choiceIndex, aScore=0, lScore=0, turn=0):
        if (len(stones) == 0):
            return (aScore > lScore)
        choiceVal = stones.pop(choiceIndex)
        if (turn == 0):
            aScore += choiceVal
            turn = 1
        else:
            lScore += choiceVal
            turn = 0
        return (self.turn(stones, (-1), aScore, lScore, turn) or self.turn(stones, 0, aScore, lScore, turn))

    def stoneGame(self, piles):
        self.a = 0
        self.l = 0
        return (self.turn(piles, (-1)) or self.turn(piles, 1))