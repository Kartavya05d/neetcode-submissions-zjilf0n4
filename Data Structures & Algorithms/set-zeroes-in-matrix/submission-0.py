class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        
        row_check = [0]*row
        col_check = [0]*col

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    row_check[i] = 1
                    col_check[j] = 1
        
        for i in range(row):
            for j in range(col):
                if row_check[i] == 1 or col_check[j] == 1:
                    matrix[i][j] = 0
        