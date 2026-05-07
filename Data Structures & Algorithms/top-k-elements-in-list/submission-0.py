import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## step 1: count the num
        num_dic = {}
        
        for n in nums:
            num_dic[n] = num_dic.get(n, 0) + 1
        
        ## step 2: use heap
        heap = []
        
        for num, count in num_dic.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for count, num in heap]