class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        #1. Transpose
        for i in range(rows):
            for j in range(i+1, rows): #transpose against diagonal.
                #swap (i,j) with (j,i)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        #2. Reverse each row
        for i in range(rows):
            matrix[i].reverse()
