class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        vertical, horizontal = 0, cols-1

        while vertical < rows and horizontal >= 0:
            if matrix[vertical][horizontal] > target:
                horizontal -= 1 #move left
            elif matrix[vertical][horizontal] < target:
                vertical += 1 #move down
            else:
                return True
        return False