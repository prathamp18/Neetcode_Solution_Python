class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def dfs(r,c):
            if 0<=r<n and 0<=c<m and grid[r][c] =='1':
                grid[r][c] = '0'
                dfs(r-1,c)
                dfs(r+1,c)
                dfs(r,c+1)
                dfs(r,c-1)
            else:
                return
        num_island = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    num_island +=1
                    dfs(i,j)
        return num_island