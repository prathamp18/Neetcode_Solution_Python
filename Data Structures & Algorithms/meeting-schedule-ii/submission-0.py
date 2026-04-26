"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)
        s = e = 0
        used_rooms = 0
        max_rooms = 0

        while s < len(intervals):
            # need a new room
            if starts[s] < ends[e]:
                used_rooms += 1
                max_rooms = max(max_rooms, used_rooms)
                s += 1
            else:
                # free a room
                used_rooms -= 1
                e += 1
        return max_rooms