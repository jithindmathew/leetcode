class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        a = 120

        for i in range(len(matrix)):
            if matrix[i][0] > target:
                a = i - 1
                break

        if a < 0:
            return False
        elif a == 120:
            for i in matrix[-1]:
                if i == target:
                    return True
        else:
            for i in matrix[a]:
                if target == i:
                    return True
            return False


        """

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False
