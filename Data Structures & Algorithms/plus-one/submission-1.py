class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''.join([str(i) for i in digits])
        plus = int(num) + 1

        return list(str(plus))

