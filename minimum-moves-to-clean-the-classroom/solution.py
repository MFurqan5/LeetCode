from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])

        start = None
        litter_id = {}
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter_id[(i, j)] = len(litter_id)

        total = len(litter_id)
        if total == 0:
            return 0

        full_mask = (1 << total) - 1
        sr, sc = start

        visited = [[[-1] * (1 << total) for _ in range(n)] for _ in range(m)]
        visited[sr][sc][0] = energy

        q = deque()
        q.append((sr, sc, energy, 0, 0))  # r, c, energy, mask, moves

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c, e, mask, moves = q.popleft()

            if mask == full_mask:
                return moves

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if classroom[nr][nc] == 'X':
                    continue

                if e == 0:
                    continue

                new_e = e - 1

                if classroom[nr][nc] == 'R':
                    new_e = energy

                new_mask = mask
                if classroom[nr][nc] == 'L':
                    idx = litter_id[(nr, nc)]
                    new_mask = mask | (1 << idx)

                if visited[nr][nc][new_mask] < new_e:
                    visited[nr][nc][new_mask] = new_e
                    q.append((nr, nc, new_e, new_mask, moves + 1))

        return -1