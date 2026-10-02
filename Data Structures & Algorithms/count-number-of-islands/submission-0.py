class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = []

        def search(row, col):
            if grid[row][col] != '1':
                return
            visited.append([row, col])
            if row+1 < len(grid) and [row+1, col] not in visited:
                search(row+1, col)
            if row-1 >= 0 and [row-1, col] not in visited:
                search(row-1, col)
            if col + 1 < len(grid[0]) and [row, col+1] not in visited:
                search(row, col+1)
            if col - 1 >= 0 and [row, col-1] not in visited:
                search(row, col-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and [i, j] not in visited:
                    count += 1
                    search(i, j)

        return count
                



                    

        