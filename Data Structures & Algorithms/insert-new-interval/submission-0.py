class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        ns, ne = newInterval[0], newInterval[1]

        for i in range(len(intervals)):
            if intervals[i][1] < ns:
                res.append(intervals[i])
            elif intervals[i][0] > ne:
                res.append([ns, ne])
                res += intervals[i::]
                return res
            else:
                ns = min(ns, intervals[i][0])
                ne = max(ne, intervals[i][1])
                
        res.append([ns,ne])
        
        return res