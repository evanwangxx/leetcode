# Given an 2D board, count how many battleships are in it.
# The battleships are represented with 'X's, empty slots are represented with '.'s.
# You may assume the following rules:
#   1. You receive a valid board, made of only battleships or empty slots.
#   2. Battleships can only be placed horizontally or vertically.
#       In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column),
#       where N can be of any size.
#   3. At least one horizontal or vertical cell separates between two battleships
#       - there are no adjacent battleships.
#
# Example:
#           X..X
#           ...X
#           ...X
# In the above board there are 2 battleships.
# Invalid Example:
#           ...X
#           XXXX
#           ...X
# This is an invalid board that you will not receive
# - as battleships will always have a cell separating between them.


class Solution:
    def countBattleships(self, board):
        if not board:
            return 0
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    count += 1
                    self.dfs_search(i, j, board)
        return count

    def dfs_search(self, i, j, board):
        if board[i][j] == "X":
            board[i][j] = "x"
            if i + 1 < len(board):
                self.dfs_search(i+1, j, board)
            if j + 1 < len(board[0]):
                self.dfs_search(i, j+1, board)
        else:
            return


test = [["X", ".", ".", "X"],
        [".", ".", ".", "X"],
        [".", ".", ".", "X"]]
print(Solution().countBattleships(test))
