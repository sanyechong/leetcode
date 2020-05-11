'''Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''



class Solution:
    def maximalSquare(self, matrix: [[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        maxSide = 0
        width = len(matrix[0])
        height = len(matrix)

        for i in range(height):
            for j in range(width):
                if matrix[i][j] == '1':
                    # treat it as the top left corner of the square
                    maxSide = max(maxSide, 1)
                    curMaxSide = min(height-i, width-j)
                    # point i,j --> i+k,j+k make a square
                    for k in range(curMaxSide):
                        flag = True
                        # first diagonal
                        if matrix[i+k][j+k] == '0':
                            break
                        # then side
                        for m in range(k):
                            if matrix[i+k][j+m] == '0' or matrix[i+m][j+k] == '0':
                                flag = False
                                break
                        if flag:
                            maxSide = max(maxSide, k+1)
                        else:
                            break
        return (maxSide ** 2)



if __name__ == '__main__':
    s = Solution()
    print(s.maximalSquare([["0","1","1","0","1"],["1","1","0","1","0"],["0","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["0","0","0","0","0"]]))

