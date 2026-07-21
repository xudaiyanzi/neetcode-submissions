"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [m.start for m in intervals]
        ends = [m.end for m in intervals]
        starts.sort()
        ends.sort()

        max_rooms, curr_rooms = 0, 0
        i, j = 0, 0

        while i < len(starts):
            if starts[i] < ends[j]:
                curr_rooms += 1
                i += 1
            else:
                curr_rooms -= 1
                j += 1
            max_rooms = max(max_rooms, curr_rooms)
        return max_rooms