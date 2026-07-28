class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        zeros = []

        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 0:
                    zeros.append([r,c])
        
        for r, c in zeros:
            for i in range(n):
                matrix[i][c] = 0
            for j in range(m):
                matrix[r][j] = 0

