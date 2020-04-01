# 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
# 路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
# 如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
# 例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。
#
#   [["a","b","c","e"],
#    ["s","f","c","s"],
#    ["a","d","e","e"]]
#
# 但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
#
# 示例 1：
#   输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
#   输出：true
#
# 示例 2：
#   输入：board = [["a","b"],["c","d"]], word = "abcd"
#   输出：false
#
# 提示：
#   1 <= board.length <= 200
#   1 <= board[i].length <= 200


class Solution:
    def exist(self, board, word):
        if not board or not word:
            return True

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs_search(i, j, board, word):
                        return True
        return False

    def dfs_search(self, i, j, grid, tar_string):
        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1:
            return False
        if len(tar_string) == 1 and grid[i][j] == tar_string[0]:
            return True
        elif grid[i][j] != tar_string[0]:
            return False

        tmp = grid[i][j]
        grid[i][j] = "$"
        result = self.dfs_search(i + 1, j, grid, tar_string[1:]) or \
                 self.dfs_search(i - 1, j, grid, tar_string[1:]) or \
                 self.dfs_search(i, j + 1, grid, tar_string[1:]) or \
                 self.dfs_search(i, j - 1, grid, tar_string[1:])
        grid[i][j] = tmp

        return result


x = [["C", "A", "A"],
     ["A", "A", "A"],
     ["B", "C", "D"]]

x2 = [["A", "B", "C", "E"],
      ["S", "F", "E", "S"],
      ["A", "D", "E", "E"]]
y2 = "ABCESEEEFS"

x3 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
y3 = "ABCB"

x4 = [["a", "a", "a", "a"], ["a", "a", "a", "a"], ["a", "a", "a", "a"], ["a", "a", "a", "a"],
      ["a", "a", "a", "b"]]
y4 = "aaaaaaaaaaaaaaaaaaaa"

x = [x, x2, x3, x4]
y = ["ABC", y2, y3, y4]
for i, j in zip(x, y):
    print(Solution().exist(i, j))
