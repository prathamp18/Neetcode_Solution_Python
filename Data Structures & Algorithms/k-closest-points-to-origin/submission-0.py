class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        dist = []
        for pt in points:
            dist = math.sqrt(math.pow(pt[0], 2) + math.pow(pt[1], 2))
            heapq.heappush(heap, (-dist, pt))
            if len(heap)>k:
                heapq.heappop(heap)

        return [pt for dist, pt in heap]