class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direction = [[-1,0], [0,1], [0, -1], [1,0]]
        count = 0
        rows, cols = len(grid), len(grid[0])
        def isValid(row, col):
            return 0<=row<rows and 0<=col<cols
        
        def dfs(row, col):
            if not isValid(row, col) or grid[row][col] !=1:
                return 0
            grid[row][col] = 2
            curr_count = 1
            for d in direction:
                curr_count += dfs(row+d[0], col+d[1])
            return curr_count
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count = max(count, dfs(i,j))
        return count