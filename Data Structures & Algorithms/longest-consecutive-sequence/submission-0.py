class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in s:
            if num - 1 not in s:  # start of sequence
                current = num
                streak = 1

                while current + 1 in s:
                    current += 1
                    streak += 1

                longest = max(longest, streak)

        return longest