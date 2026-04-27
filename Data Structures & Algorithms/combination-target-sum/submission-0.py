class Solution:
    def solve(self, idx, total, subset, nums, result, target):
        if total == target:
            result.append(subset.copy())
            return
        if total > target:
            return
        if idx >= len(nums):
            return
        Sum = total+nums[idx]
        subset.append(nums[idx])
        self.solve(idx, Sum, subset, nums, result, target)
        Sum = total
        subset.pop()
        self.solve(idx+1, Sum, subset, nums, result, target)
    def combinationSum(self, candidate: List[int], target: int) -> List[List[int]]:
        result = []
        self.solve(0,0,[],candidate,result, target)
        return result