class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        max_freq = max(freq.values())
        buckets = [[] for _ in range(max_freq + 1)]        
        for num, count in freq.items():
            buckets[count].append(num)
        result = []
        for i in range(len(buckets)-1, 0, -1):
            result.extend(buckets[i])
            if len(result) >= k:
                break        
        return result[:k]