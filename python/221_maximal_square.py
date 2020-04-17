# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
# Example:
#   Input:
#             1 0 1 0 0
#             1 0 1 1 1
#             1 1 1 1 1
#             1 0 0 1 0
#   Output: 4


class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0

        len_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        max_len = 0

        for i in range(len(len_matrix)):
            for j in range(len(len_matrix[0])):
                if i == 0 or j == 0:
                    len_matrix[i][j] = 1 if matrix[i][j] == "1" else 0
                else:
                    if matrix[i][j] == "1":
                        len_matrix[i][j] = min(len_matrix[i - 1][j - 1],
                                               len_matrix[i - 1][j],
                                               len_matrix[i][j - 1]) + 1
                max_len = max(len_matrix[i][j], max_len)
        return max_len ** 2



test = [["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]]

print(Solution().maximalSquare(test))
