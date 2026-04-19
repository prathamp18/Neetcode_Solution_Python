class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mp = {}

        for num in nums:
            mp[num] = 1 + mp.get(num, 0)
        
        for key, val in mp.items():
            if val > 1:
                return key
