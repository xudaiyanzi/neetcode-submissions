import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followSet = defaultdict(set)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        h = []
        self.followSet[userId].add(userId)

        for followeeId in self.followSet[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(h, [count, tweetId, followeeId, index - 1])
        while h and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(h)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(h, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followSet[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followSet[followerId]:
            self.followSet[followerId].remove(followeeId)
