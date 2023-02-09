# Time:  O(k * m * n), k is the number of the buildings
# Space: O(m * n)

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def bfs(grid, dists, cnts, x, y):
            dist, m, n = 0, len(grid), len(grid[0])
            visited = [[False for _ in xrange(n)] for _ in xrange(m)]
    
            pre_level = [(x, y)]
            visited[x][y] = True
            while pre_level:
                dist += 1
                cur_level = []
                for i, j in pre_level:
                    for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        I, J = i+dir[0], j+dir[1]
                        if 0 <= I < m and 0 <= J < n and grid[I][J] == 0 and not visited[I][J]:
                            cnts[I][J] += 1
                            dists[I][J] += dist
                            cur_level.append((I, J))
                            visited[I][J] = True
    
                pre_level = cur_level


        m, n, cnt = len(grid),  len(grid[0]), 0
        dists = [[0 for _ in xrange(n)] for _ in xrange(m)]
        cnts = [[0 for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    cnt += 1
                    bfs(grid, dists, cnts, i, j)

        shortest = float("inf")
        for i in xrange(m):
            for j in xrange(n):
                if dists[i][j] < shortest and cnts[i][j] == cnt:
                    shortest = dists[i][j]

        return shortest if shortest != float("inf") else -1
