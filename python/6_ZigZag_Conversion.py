# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);
#
# Example 1:
#       Input: s = "PAYPALISHIRING", numRows = 3
#       Output: "PAHNAPLSIIGYIR"
# Example 2:
#       Input: s = "PAYPALISHIRING", numRows = 4
#       Output: "PINALSIGYAHRPI"
#       Explanation:
#               P     I    N
#               A   L S  I G
#               Y A   H R
#               P     I


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1:
            return s
        matrix = [["" for _ in range(len(s))] for _ in range(numRows)]
        pos_ls = []
        i = j = 0
        while j <= len(s)-1:
            next_start, next_pos = self.get_next_position(i, j, numRows)
            i = next_start[0]
            j = next_start[1]
            pos_ls.extend(next_pos)

        index = 0
        for c in s:
            x = pos_ls[index][0]
            y = pos_ls[index][1]
            matrix[x][y] = c
            index += 1

        res = ""
        for r in matrix:
            res += "".join(r)
        return res

    def get_next_position(self, i, j, nrow):
        next_pos = []
        c = 0
        while c < (nrow-1)*2:
            next_pos.append((i, j))
            if c >= nrow-1:
                i -= 1
                j += 1
            elif c < nrow-1:
                i += 1
            c += 1
        return (next_pos[-1][0]-1, next_pos[-1][1]+1), next_pos



s = "PAYPALISHIRING"
numRows = 3
print(Solution().convert(s, numRows), "PAHNAPLSIIGYIR")

s = "PAYPALISHIRING"
numRows = 4
print(Solution().convert(s, numRows), "PINALSIGYAHRPI")

s = "A"
numRows = 1
print(Solution().convert(s, numRows), "A")