class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [[-1,0], [0,1], [0,-1], [1,0]]
        rows, cols = len(grid), len(grid[0])
        count = 0
        def isValid(row, col):
            return 0<= row<rows and 0<=col<cols

        def dfs(row, col):
            if not isValid(row, col) or grid[row][col] != '1':
                return
            
            grid[row][col] = '2'
            for d in direction:
                new_row = row + d[0]
                new_col = col + d[1]
                dfs(new_row, new_col)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count+=1
                    dfs(i,j)
                    
        return count