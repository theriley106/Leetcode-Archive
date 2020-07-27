import string
diction = {}
MAIN = list(string.printable)
for (i, letter) in enumerate(MAIN):
    diction[str(i)] = letter


class Codec:

    def encode(self, longUrl):
        new = ''
        for letter in longUrl:
            new = ((new + '-') + str(MAIN.index(letter)))
        print new
        return new

    def decode(self, shortUrl):
        decoded = ''
        for num in shortUrl.split('-'):
            try:
                decoded = (decoded + str(diction[str(num)]))
            except:
                pass
        return decoded
