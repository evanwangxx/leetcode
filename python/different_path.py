# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        x = self.dp(m - 1, n - 1, 0, {})
        return x

    def dp(self, x, y, count, dic):
        k = str(x) + "-" + str(y)
        if k in dic.keys():
            return dic[str(x) + "-" + str(y)]

        if x == 0 or y == 0:
            dic[k] = 1
        else:
            dic[k] = self.dp(x, y-1, count, dic) + self.dp(x-1, y, count, dic)
        return dic[k]

print(Solution().uniquePaths(3, 2))
print(Solution().uniquePaths(7, 3))
print(Solution().uniquePaths(23, 12))
