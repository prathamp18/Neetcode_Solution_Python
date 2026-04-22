class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = Counter(nums)
        res = []
        heap = []
        for key, val in mp.items():
            heapq.heappush(heap, (-val, key))
        
        for i in range(0,k):
            res.append(heapq.heappop(heap)[1])
        
        return res