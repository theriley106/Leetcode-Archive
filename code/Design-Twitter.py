class Twitter(object, ):

    def __init__(self):
        self.tweets = {}
        self.followDB = {}
        self.count = 0

    def postTweet(self, userId, tweetId):
        self.count += 1
        if (userId not in self.tweets):
            self.tweets[userId] = []
        self.tweets[userId].append({'count': self.count, 'tweet': tweetId})

    def getNewsFeed(self, userId):
        a = []
        if (userId in self.tweets):
            for tweet in self.tweets[userId]:
                if (tweet not in a):
                    a.append(tweet)
        if (userId in self.followDB):
            for t in self.followDB[userId]:
                if (t in self.tweets):
                    for tweet in self.tweets[t]:
                        if (tweet not in a):
                            a.append(tweet)
        recentNums = []
        for val in a:
            recentNums.append(int(val['count']))
        toReturn = []
        toFind = sorted(recentNums, reverse=True)[:10]
        print toFind
        for v in toFind:
            for val in a:
                if (int(val['count']) == v):
                    toReturn.append(val['tweet'])
        return toReturn

    def follow(self, followerId, followeeId):
        if (followerId not in self.followDB):
            self.followDB[followerId] = []
        self.followDB[followerId].append(followeeId)

    def unfollow(self, followerId, followeeId):
        if (followerId in self.followDB):
            if (followeeId in self.followDB[followerId]):
                self.followDB[followerId].remove(followeeId)