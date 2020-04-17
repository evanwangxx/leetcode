# Given two strings text1 and text2, return the length of their longest common subsequence.
#
# A subsequence of a string is a new string generated from the original string with some
# characters(can be none) deleted without changing the relative order of the remaining characters.
# (eg, "ace" is a subsequence of "abcde" while "aec" is not). 
# A common subsequence of two strings is a subsequence that is common to both strings.
#
# If there is no common subsequence, return 0.
#
# Example 1:
#       Input: text1 = "abcde", text2 = "ace"
#       Output: 3
#       Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:
#       Input: text1 = "abc", text2 = "abc"
#       Output: 3
#       Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:
#       Input: text1 = "abc", text2 = "def"
#       Output: 0
#       Explanation: There is no such common subsequence, so the result is 0.
#  
# Constraints:
#       1 <= text1.length <= 1000
#       1 <= text2.length <= 1000
#       The input strings consist of lowercase English characters only.


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.dp_iterate(text1, text2)

    def dp_recursion(self, text1: str, text2: str) -> int:
        dp_table = [[None for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        def dp_helper(i, j):
            if dp_table[i][j]:
                return dp_table[i][j]

            if i == 0 or j == 0:
                dp_table[i][j] = 0
            else:
                if text1[i-1] == text2[j-1]:
                    dp_table[i][j] = dp_helper(i - 1, j - 1) + 1
                else:
                    dp_table[i][j] = max(dp_helper(i - 1, j - 1),
                                         dp_helper(i - 1, j),
                                         dp_helper(i, j - 1))
            return dp_table[i][j]
        res = dp_helper(len(text1), len(text2))
        for l in dp_table:
            print(l)
        return res

    def dp_iterate(self, text1: str, text2: str) -> int:
        dp_table = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp_table[i][j] += dp_table[i-1][j-1] + 1
                else:
                    dp_table[i][j] += max(dp_table[i - 1][j - 1], dp_table[i - 1][j], dp_table[i][j - 1])
        for l in dp_table:
            print(l)
        return dp_table[-1][-1]

print(Solution().longestCommonSubsequence("abcde", "ace"), 3)
print(Solution().longestCommonSubsequence("abcde", ""), 0)
print(Solution().longestCommonSubsequence("bsbininm", "jmjkbkjkv"), 1)
