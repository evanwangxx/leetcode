# Given a string which consists of lowercase or uppercase letters,
# find the length of the longest palindromes that can be built with those letters.
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note: Assume the length of given string will not exceed 1,010.
# Example:
#   Input: "abccccdd"
#   Output: 7
#   Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

class Solution:
    def longestPalindrome(self, s):
        dic = {}
        for c in s:
            if c in dic.keys():
                dic[c] += 1
            else:
                dic[c] = 1

        res = 0
        exist_odd = 0
        for k in dic.keys():
            if dic[k] % 2 != 0 and dic[k] - 1 >= 0:
                res += dic[k] - 1
                exist_odd = 1
            else:
                res += dic[k]
        return res + exist_odd


x = "abccccdd"
print(Solution().longestPalindrome(x), 7)


x = "aabaabdd"
print(Solution().longestPalindrome(x), 8)
