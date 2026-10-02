class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = (len(matrix) * len(matrix[0])) - 1
        l = 0
        m = math.trunc((r-l)/2)
        cur = matrix[math.trunc(m/len(matrix[0]))][m % len(matrix[0])]
        while cur != target:
            if r-l <= 1:
                if matrix[math.trunc(l/len(matrix[0]))][l % len(matrix[0])] == target or matrix[math.trunc(r/len(matrix[0]))][r % len(matrix[0])] == target:
                    return True
                return False
            if cur < target:
                l = m
            else:
                r = m
            m = math.trunc((r-l)/2) + l
            cur = matrix[math.trunc(m/len(matrix[0]))][m % len(matrix[0])]
            print(cur)
            print(m)
            print(l)
            print(r)
        return True
                 