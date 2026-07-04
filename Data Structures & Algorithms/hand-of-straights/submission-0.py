class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    
        hand_dic = {}

        for h in hand:
            hand_dic[h] = hand_dic.get(h, 0) + 1
        
        while hand_dic:
            small_key = min(hand_dic) # key
            small_val = hand_dic[small_key]

            for i in range(small_key, small_key + groupSize):
                if i not in hand_dic or hand_dic[i] < small_val:
                    return False
                hand_dic[i] -= 1
                if hand_dic[i] == 0:
                    del hand_dic[i]
        
        return True
        
        
            