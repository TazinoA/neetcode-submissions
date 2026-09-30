import time
import heapq
"""
userToPost = {
   1:[1,2,3,4,5,6,7,8,9,10,11]
}
followingMap = {
    5:[5]
}
"""
class Twitter:

    def __init__(self):
        self.userToPost = {}
        self.followingMap = {}
        self.time = 0
    """
    keep user to post map, so when we check user following,
    we can loop through each of their posts
    """
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userToPost:
            self.userToPost[userId] = []
        self.userToPost[userId].append([self.time, tweetId])
        self.time += 1
    """
    max heap to store 10 most recent tweets, so when we add new tweet,
    we can pop the max tweet cause it would be the least recent,
    this keeps the most recent tweets in the heap
    """
    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        for followeeId in self.followingMap.get(userId, {userId}):
            for tweet in self.userToPost.get(followeeId, []):
                heapq.heappush(maxHeap, tweet)
                while len(maxHeap) > 10:
                    heapq.heappop(maxHeap)
        res = []
        while maxHeap:
            res.append(heapq.heappop(maxHeap)[1])
        return res[::-1]

    """
    keep user following map for user to their followings
    """
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followingMap:
            self.followingMap[followerId] = set([followerId])
        self.followingMap[followerId].add(followeeId)
    """
    remove followee from followers map
    """
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followingMap and followerId != followeeId:
            if followeeId in self.followingMap[followerId]:
                self.followingMap[followerId].remove(followeeId)
