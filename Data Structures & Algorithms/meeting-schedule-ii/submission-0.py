"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda pair: pair.start)
        min_heap = []
        for interval in intervals:
            #Earliest endtime is compared with current interval's start time.
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap) #reusing the room with new end time.
            heapq.heappush(min_heap, interval.end) #using the room till current end
        return len(min_heap)
