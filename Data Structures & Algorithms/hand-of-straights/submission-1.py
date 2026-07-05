class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        
        counts = Counter(hand)

        for key in sorted(counts):
            c = counts[key]
            if c > 0:
                for k in range(key, key + groupSize):
                    if counts[k] < c:
                        return False
                    counts[k] -= c
        
        return True
        
            