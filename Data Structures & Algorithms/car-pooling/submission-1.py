import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t:t[1])
        h = [] # only[end, num]
        curr_total = 0

        for num, start, end in trips:
            while h and h[0][0] <= start:
                curr_end, curr_num = heapq.heappop(h)
                curr_total -= curr_num

            curr_total += num
            if curr_total > capacity:
                return False

            heapq.heappush(h, [end, num])
        
        return True
        


        