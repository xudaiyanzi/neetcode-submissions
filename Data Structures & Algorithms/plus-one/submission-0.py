class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0

        for d in digits:
            res = res * 10 + d
        
        res += 1
        res_s = str(res)
        return list(res_s)

