"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda Interval: Interval.start)
        if intervals:
            pre_e = intervals[0].end 
        else: 
            return True

        for i in intervals[1:]:
            if i.start >= pre_e:
                pre_e = i.end
            else:
                return False
        
        return True
