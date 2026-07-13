class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = 0, 0 ,0
        for item in triplets:
            if item[0] > target[0] or item[1] > target[1] or item[2] > target[2]:
                continue
            a = max(a, item[0])
            b = max(b, item[1])
            c = max(c, item[2])
            if [a, b, c] == target: 
                return True
        return False