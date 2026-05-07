from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dic = defaultdict(list)

        for s in strs:
            sorted_s = ''.join(sorted(s))
            str_dic[sorted_s].append(s)
        
        return list(str_dic.values())