import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ''
        waiting = []
        if a: waiting.append((-a, 'a'))
        if b: waiting.append((-b, 'b'))
        if c: waiting.append((-c, 'c'))
        heapq.heapify(waiting)
        
        hold = None
        while waiting:
            val, char = heapq.heappop(waiting)
            n = len(res)
            if n >= 2 and res[-2] == char and res[-1] == char:
                if not waiting:
                    break
                
                val2, char2 = heapq.heappop(waiting)
                res += char2
                val2 += 1
                if val2 < 0: 
                    heapq.heappush(waiting, (val2, char2))
                heapq.heappush(waiting, (val, char))
                    
            else:
                res += char
                val += 1
                if val < 0: 
                    heapq.heappush(waiting, (val, char))
        
        return res
            
