# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#   'A' -> 1
#   'B' -> 2
#       ...
#   'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
#
# Example 1:
#       Input: "12"
#       Output: 2
#       Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:
#       Input: "226"
#       Output: 3
#       Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).


class Solution:
    def numDecodings(self, s):
        chars = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(",")
        dict = {}
        for i in range(1, 27):
            dict[i] = chars[i-1]
        return self.decode(0, s, dict)

    def decode(self, i, s, dict):
        if i == len(s)-1:
            return 1 if int(s[i]) in dict.keys() else 0
        if i == len(s)-2:
            if int(s[i:]) in {10, 20}:
                return 1

            if int(s[i:]) in dict.keys():
                return 2

            return 2 if int(s[i:]) in dict.keys() else 1
        elif i > len(s)-1:
            return 0

        if int(s[i] + s[i+1]) in dict.keys():
            return self.decode(i+1, s, dict) + self.decode(i+2, s, dict)
        else:
            return 0

x = "12"
print(Solution().numDecodings(x), 2)

x = "0"
print(Solution().numDecodings(x), 0)

x = "10"
print(Solution().numDecodings(x), 1)

x = "12"
print(Solution().numDecodings(x), 2)

x = "226"
print(Solution().numDecodings(x), 3)


