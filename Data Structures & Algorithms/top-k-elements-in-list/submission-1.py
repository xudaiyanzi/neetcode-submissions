import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for n in nums:
            dic[n] = dic.get(n, 0) + 1

        heap = []
        for (n, count) in dic.items():
            heapq.heappush(heap, [-count, n])
        
        res = []
        i = 0
        while i < k:
            n = heapq.heappop(heap)[1]
            res.append(n)
            i += 1
        
        return res