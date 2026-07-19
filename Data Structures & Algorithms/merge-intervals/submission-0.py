class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        st_intervals = sorted(intervals, key = lambda x:x[0])
        res = []
        ns, ne = st_intervals[0][0], st_intervals[0][1]

        for s, e in st_intervals[1:]:
            if s > ne:
                res.append([ns, ne])
                ns, ne = s, e
            else:
                ns = min(s, ns)
                ne = max(e, ne)
        
        res.append([ns, ne])
        return res
            
            