import heapq
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k + 1):
            temp = prices.copy()

            for a, b, p in flights:
                if prices[a] == float('inf'):
                    continue
                if prices[a] + p < temp[b]:
                    temp[b] = prices[a] + p
                
            prices = temp
        
        return prices[dst] if prices[dst] != float('inf') else -1

