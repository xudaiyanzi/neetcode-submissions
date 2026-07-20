class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        sorted_in = sorted(intervals, key = lambda x: x[0])
        pre_e = sorted_in[0][1]

        for s, e in sorted_in[1:]:
            if s >= pre_e:
                pre_e = e
                continue
            else:
                if e < pre_e:
                    pre_e = e
                count += 1
        
        return count



