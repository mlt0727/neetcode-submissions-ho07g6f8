class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        ans = [[] for _ in range(length)]
        for i in range(length-1,-1,-1):
            for j in range(length):
                ans[j].append(matrix[i][j])
        for i in range(length):
            for j in range(length):
                matrix[i][j] = ans[i][j]