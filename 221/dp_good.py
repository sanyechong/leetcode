class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        height, width = len(matrix), len(matrix[0])
        if height == 0 or width == 0:
            return 0

        maxSide = 0
        dp = [[0 for x in range(width)] for y in range(height)]
        #dp = [[0]*width for _ in range(height)]
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        return maxSide ** 2
