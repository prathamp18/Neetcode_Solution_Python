class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stk = []

        for i in range(n):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                stk_i = stk.pop()
                res[stk_i] = i - stk_i
            stk.append(i)
        return res