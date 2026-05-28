import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.follow_map = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        q = []

        users = self.follow_map[userId]
        users.add(userId)

        for u in users:
            for time, tweetId in self.tweets[u][-10:]:
                heapq.heappush(q, (time, tweetId))
        
        res = []
        while q and len(res) < 10:
            time, tweetId = heapq.heappop(q)
            res.append(tweetId)
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)
        
