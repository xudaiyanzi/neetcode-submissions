import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ''
        dic = {}

        for char in s:
            dic[char] = dic.get(char, 0) - 1
        
        waiting = []
        for char, count in dic.items():
            heapq.heappush(waiting, (count, char))
        
        if abs(waiting[0][0]) > (len(s) + 1) // 2:
            return res
        
        prev = None
        while waiting or prev:
            if prev and not waiting:
                return ""

            count, char = heapq.heappop(waiting)
            res += char
            count += 1

            if prev:
                heapq.heappush(waiting, prev)
                prev = None
            
            if count != 0:
                prev = (count, char)
        
        return res

            
