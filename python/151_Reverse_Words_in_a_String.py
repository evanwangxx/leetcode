# Given an input string, reverse the string word by word.
#
# Example 1:
#   Input: "the sky is blue"
#   Output: "blue is sky the"
# Example 2:
#   Input: "  hello world!  "
#   Output: "world! hello"
#   Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:
#   Input: "a good   example"
#   Output: "example good a"
#   Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
#  
# Note:
    # A word is defined as a sequence of non-space characters.
#   Input string may contain leading or trailing spaces.
#   However, your reversed string should not contain leading or trailing spaces.
#   You need to reduce multiple spaces between two words to a single space in the reversed string.


class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack and c == " ":
                continue
            else:
                if stack and c == " ":
                    if stack[-1] == " ":
                        continue
                    else:
                        stack.append(" ")
                else:
                    stack.append(c)
        print(stack)
        # return " ".join(s)


x = "the sky is blue"
print(Solution().reverseWords(x))

x = "  hello world!  "
print(Solution().reverseWords(x))

x = "a good   example"
print(Solution().reverseWords(x))