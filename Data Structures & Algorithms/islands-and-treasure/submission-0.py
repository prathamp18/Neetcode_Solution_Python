class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        direction = [[-1,0], [0,1],[0,-1],[1,0]]
        rows = len(grid)
        cols = len(grid[0])
        if not grid:
            return
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))
        while q:
            row, col = q.popleft()
            for d in direction:
                nr, nc = row+d[0], col+d[1]
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[row][col] + 1
                    q.append((nr,nc))