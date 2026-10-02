class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        copy = grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2147483647:
                    visited = set((i, j))
                    queue = [[i, j, 0]]
                    while queue:
                        cur = queue.pop(0)
                        # is it treasure?
                        if grid[cur[0]][cur[1]] == 0:
                            copy[i][j] = min(cur[2], copy[i][j])
                        elif grid[cur[0]][cur[1]] == -1:
                            continue

                        if cur[0]+1 < len(grid) and (cur[0]+1, cur[1]) not in visited:
                            visited.add((cur[0]+1, cur[1]))
                            queue.append([cur[0]+1, cur[1], cur[2]+1])
                        if cur[0]-1 >= 0 and (cur[0]-1, cur[1]) not in visited:
                            visited.add((cur[0]-1, cur[1]))
                            queue.append([cur[0]-1, cur[1], cur[2]+1])
                        if cur[1]+1 < len(grid[0]) and (cur[0], cur[1]+1) not in visited:
                            visited.add((cur[0], cur[1]+1))
                            queue.append([cur[0], cur[1]+1, cur[2]+1])
                        if cur[1]-1 >= 0 and (cur[0], cur[1]-1) not in visited:
                            visited.add((cur[0], cur[1]-1))
                            queue.append([cur[0], cur[1]-1, cur[2]+1])
        return copy
                    