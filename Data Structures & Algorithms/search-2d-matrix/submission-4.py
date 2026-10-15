class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==1:
            for i in matrix:
                if i==target:
                    return True
            return False
        elif len(matrix)>1:
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    if matrix[i][j]==target:
                        return True
            return False
        else:
            return False