# Given an integer n, return 1 - n in lexicographical order.
#
# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
#
# Please optimize your algorithm to use less time and space.
# The input size may be as large as 5,000,000.


class Solution:
    def lexicalOrder(self, n):
        res = []
        for d in range(1, 10):
            self.dfs(d, n, res)
        return res

    def dfs(self, num, n, res):
        if num > n:
            return None

        res.append(num)
        for d in range(10):
            self.dfs(num*10 + d, n, res)


print(Solution().lexicalOrder(13))
