class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        res = []
        start, end = intervals[0]
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s <= end:
                end = max(end, e)
            else:
                res.append([start, end])
                start, end = s, e
        res.append([start, end])
        return res
            
             