# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
# You have the following 3 operations permitted on a word:
#       Insert a character
#       Delete a character
#       Replace a character
#
# Example 1:
#   Input: word1 = "horse", word2 = "ros"
#   Output: 3
#   Explanation:
#         horse -> rorse (replace 'h' with 'r')
#         rorse -> rose (remove 'r')
#         rose -> ros (remove 'e')
# Example 2:
#   Input: word1 = "intention", word2 = "execution"
#   Output: 5
#   Explanation:
#         intention -> inention (remove 't')
#         inention -> enention (replace 'i' with 'e')
#         enention -> exention (replace 'n' with 'x')
#         exention -> exection (replace 'n' with 'c')
#         exection -> execution (insert 'u')


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # return self.dp_table(word1, word2)
        if not word1 or not word2:
            return len(word1) if not word2 else len(word2)
        dic = {}
        return self.dp_force(word1, word2, len(word1) - 1, len(word2) - 1, dic)

    def dp_force(self, w1, w2, i, j, dic):
        # bad case: if empty string, return the other one
        if (i, j) in dic:
            return dic[(i, j)]
        if i == -1:
            dic[(i, j)] = j + 1
        elif j == -1:
            dic[(i, j)] = i + 1
        else:
            # nothing need to do
            if w1[i] == w2[j]:
                dic[(i, j)] = self.dp_force(w1, w2, i - 1, j - 1, dic)
            else:
                add = 1 + self.dp_force(w1, w2, i, j - 1, dic)
                delete = 1 + self.dp_force(w1, w2, i - 1, j, dic)
                edit = 1 + self.dp_force(w1, w2, i - 1, j - 1, dic)
                dic[(i, j)] = min(add, delete, edit)
        return dic[(i, j)]

    def dp_table(self, w1, w2):
        table = [[None for _ in range(len(w2) + 1)] for _ in range(len(w1) + 1)]
        def helper(i, j):
            if table[i][j]:
                return table[i][j]
            if i == 0 and j == 0:
                table[i][j] = 0
            elif i == 0 and j != 0:
                table[i][j] = helper(i, j - 1) if w1[i-1] == w2[j-1] else helper(i, j - 1) + 1
            elif i != 0 and j == 0:
                table[i][j] = helper(i - 1, j) if w1[i-1] == w2[j-1] else helper(i - 1, j) + 1
            else:
                if w1[i-1] == w2[j-1]:
                    table[i][j] = min(helper(i-1, j-1), helper(i-1, j), helper(i, j-1))
                else:
                    table[i][j] = min(helper(i-1, j-1), helper(i-1, j), helper(i, j-1)) + 1
            return table[i][j]
        res = helper(len(w1), len(w2))
        for l in table:
            print(l)
        return res


print(Solution().minDistance("horse", "ros"), 3)
print(Solution().minDistance("intention", "execution"), 5)
print(Solution().minDistance("", "a"), 1)
