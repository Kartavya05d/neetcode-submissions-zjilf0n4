class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        row_ptr, col_ptr = 0, cols-1

        while row_ptr < rows and col_ptr >= 0:
            current_value = matrix[row_ptr][col_ptr]
            if current_value == target:
                return True
            elif current_value < target:
                row_ptr += 1
            else:
                col_ptr -= 1
        return False