class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda pair: pair[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if res[-1][1] <= intervals[i][0]:
                res.append(intervals[i])
            else:
                #When two intervals overlap, discard the one with the later ending time. (greedy) so that we have more space to accomodate.
                if intervals[i][1] < res[-1][1]:
                    res[-1] = intervals[i]
        return len(intervals)-len(res)
