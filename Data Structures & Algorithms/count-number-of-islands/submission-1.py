class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        island = 0
        def bfs(r, c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            while q:
                rr, cc = q.popleft()
                for dr, dc in directions:
                    roww, coll = dr+rr, dc+cc
                    if (
                        roww in range(ROWS) and
                        coll in range(COLS) and
                        grid[roww][coll] == "1" and
                        (roww, coll) not in visit
                    ):
                        q.append((roww, coll))
                        visit.add((roww, coll))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visit:
                    bfs(r,c)
                    island+=1
        return island
                    