class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])
        top, bottom = 0, row-1
        left, right = 0, col-1
        res = []
        while left <= right and top <= bottom:
            #cover top
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top+=1
            #cover right col
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right-=1

            if not (left <= right and top <= bottom): break

            #cover bottom
            for i in range(right, left-1, -1):
                res.append(matrix[bottom][i])
            bottom-=1
            #cover left col
            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
            left+=1
        return res
