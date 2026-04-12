class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for num in nums:
            if num not in a:
                a.add(num)
            else:
                return True
        return False