class TweetCounts(object, ):

    def __init__(self):
        self.db = {}

    def recordTweet(self, tweetName, time):
        if (tweetName not in self.db):
            self.db[tweetName] = []
        self.db[tweetName].append(time)
        self.db[tweetName].sort()

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        if (freq == 'hour'):
            interVals = (((endTime - startTime) / (60 * 60)) + 1)
        elif (freq == 'minute'):
            interVals = (((endTime - startTime) / 60) + 1)
        else:
            interVals = (((endTime - startTime) / ((60 * 60) * 60)) + 1)
        a = []
        while (startTime <= endTime):
            total = 0
            if (freq == 'minute'):
                for val in self.db[tweetName]:
                    if (val >= startTime):
                        if (val < min((startTime + 60), (endTime + 1))):
                            total += 1
                        else:
                            break
                startTime += 60
            elif (freq == 'hour'):
                for val in self.db[tweetName]:
                    if (val >= startTime):
                        if (val < min((startTime + (60 * 60)), (endTime + 1))):
                            total += 1
                        else:
                            break
                startTime += (60 * 60)
            else:
                for val in self.db[tweetName]:
                    if (val >= startTime):
                        if (val < min((startTime + ((60 * 60) * 60)), (endTime + 1))):
                            total += 1
                        else:
                            break
                startTime += ((60 * 60) * 60)
            a.append(total)
        return a
        return [int((float(total) / interVals))]