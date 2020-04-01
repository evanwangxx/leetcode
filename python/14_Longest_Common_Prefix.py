# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


class Solution:
    @staticmethod
    def find_common_between_string(cs, y):
        if not cs or not y:
            return ""
        cm = ""
        for i in range(min(len(cs), len(y))):
            if cs[i] == y[i]:
                cm += cs[i]
            else:
                return cm
        return cm

    def longestCommonPrefix(self, strs: [str]) -> str:
        if not strs:
            return ""
        common_prefix = strs[0]
        for i in range(1, len(strs)):
            this = strs[i]
            common_prefix = self.find_common_between_string(common_prefix, this)
        return common_prefix


t1 = ["flower", "flow", "flight"]
t2 = ["dog", "racecar", "car"]

print(Solution().longestCommonPrefix(t1))
print(Solution().longestCommonPrefix(t2))