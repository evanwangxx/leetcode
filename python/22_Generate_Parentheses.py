# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#       [    "((()))",
#            "(()())",
#            "(())()",
#            "()(())",
#            "()()()"    ]

class Solution:
    def __init__(self):
        self.res = []

    def generateParenthesis(self, n):
        if n == 0:
            return []
        elif n == 1:
            return ["()"]
        self.generate_parenthesis_helper("", 0, n*2)
        return self.res

    def generate_parenthesis_helper(self, res, front_cnt, n):
        if n == 0:
            self.res.append(res)
        elif front_cnt == 0:
            self.generate_parenthesis_helper(res+"(", front_cnt+1, n-1)
        else:
            if front_cnt < n:
                self.generate_parenthesis_helper(res+"(", front_cnt+1, n-1)
            if front_cnt > 0:
                self.generate_parenthesis_helper(res+")", front_cnt-1, n-1)


for l in Solution().generateParenthesis(3):
    print(l)


