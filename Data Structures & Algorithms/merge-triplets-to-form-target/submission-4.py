class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = False, False, False
        for item in triplets:
            a = a | (item[0] == target[0] and item[1] <= target[1] and item[2] <= target[2])
            b = b | (item[0] <= target[0] and item[1] == target[1] and item[2] <= target[2])
            c = c | (item[0] <= target[0] and item[1] <= target[1] and item[2] == target[2])
        return a and b and c