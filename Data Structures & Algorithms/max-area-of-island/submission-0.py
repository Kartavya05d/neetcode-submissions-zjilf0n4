class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        directions = [
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        ]
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = 0
            area = 1
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    roww, coll = dr+row,dc+col
                    if(
                        roww in range(ROWS) and
                        coll in range(COLS) and
                        grid[roww][coll] == 1
                    ):
                        grid[roww][coll] = 0
                        area+=1
                        q.append((roww, coll))
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    a = bfs(r,c)
                    max_area = max(max_area, a)
        return max_area

