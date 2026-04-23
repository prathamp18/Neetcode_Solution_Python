class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            if matrix[i][0] <= target <= matrix[i][c-1]:
                l = 0
                right = c-1

                while l<=right:
                    mid = (l+right) // 2
                    if matrix[i][mid] == target:
                        return True
                    if matrix[i][mid] > target:
                        right = mid - 1
                    else:
                        l = l+1
        return False
