from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.counter += 1
        self.tweetMap[userId].append([self.counter, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        userList = [userId]
        for user in self.followMap[userId]:
            userList.append(user)
        h = []
        for user in userList:
            tweets = self.tweetMap[user]
            n = len(tweets)
            single_h = []
            if n > 10:
                for i in range( n - 1, n - 11, -1):
                    single_h.append(tweets[i])
            else:
                single_h = tweets
            
            for i in single_h:
                heapq.heappush(h, i)
                if len(h) > 10:
                    heapq.heappop(h)
        
        while h:
            _, tweet = heapq.heappop(h)
            res.append(tweet)

        res.reverse()
        return res
            
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
