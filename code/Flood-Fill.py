class Solution(object):

    def fill(self, newsr, newsc):
        change = 0
        if (self.image[newsr][newsc] == self.color):
            self.image[newsr][newsc] = self.newColor
            if ((newsr + 1) < len(self.image)):
                print 'CALLING 8'
                if (self.image[(newsr + 1)][newsc] == self.color):
                    self.fill((newsr + 1), newsc)
            if ((newsr - 1) > (-1)):
                print 'CALLING 11'
                if (self.image[(newsr - 1)][newsc] == self.color):
                    self.fill((newsr - 1), newsc)
            if ((newsc + 1) < len(self.image[0])):
                print 'CALLING 15'
                if (self.image[newsr][(newsc + 1)] == self.color):
                    self.fill(newsr, (newsc + 1))
            if ((newsc - 1) > (-1)):
                print 'CALLING 17'
                if (self.image[newsr][(newsc - 1)] == self.color):
                    self.fill(newsr, (newsc - 1))

    def floodFill(self, image, sr, sc, newColor):
        self.newColor = newColor
        self.color = image[sr][sc]
        self.image = image
        if (self.color == newColor):
            return image
        self.fill(sr, sc)
        return self.image