# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#   Input: "abcabcbb"
#   Output: 3
#   Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
#   Input: "bbbbb"
#   Output: 1
#   Explanation: The answer is "b", with the length of 1.
#
# Example 3:
#   Input: "pwwkew"
#   Output: 3
#   Explanation: The answer is "wke", with the length of 3.
#                Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        w1 = 0
        w2 = w1
        max_len = 0
        m = {}
        while w2 != len(s):
            if s[w2] in m.keys():
                m = {}
                w1 = w1 + 1
                w2 = w1
                continue
            else:
                if w2 - w1 + 1 > max_len:
                    max_len = w2 - w1 + 1
                m[s[w2]] = 1
                w2 += 1
        return max_len


if __name__ == "__main__":
    sn = "au"
    print(Solution().lengthOfLongestSubstring(sn))
    s1 = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s1))
    s2 = "bbbbb"
    print(Solution().lengthOfLongestSubstring(s2))
    s3 = "pwwkew"
    print(Solution().lengthOfLongestSubstring(s3))