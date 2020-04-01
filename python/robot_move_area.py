# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
# 一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格
# 不能移动到方格外，也不能进入行坐标和列坐标的数位之和大于k的格子。
#
# 例如，当k为18时，
#   机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
#   但它不能进入方格 [35, 38]，因为3+5+3+8=19。
#
# 请问该机器人能够到达多少个格子？
#
#  
# 示例 1：
#   输入：m = 2, n = 3, k = 1
#   输出：3
#
# 示例 2：
#   输入：m = 3, n = 1, k = 0
#   输出：1


class Solution:
    def movingCount(self, m, n, k):
        grid = [[0 for _ in range(n)] for _ in range(m)]
        def bfs(i, j, count):
            if not 0 <= i <= m-1 or not 0 <= j <= n-1 or self.digit_add(i, j) > k or grid[i][j] != 0:
                return 0
            grid[i][j] = 1
            count = 1 + bfs(i+1, j, count) + bfs(i-1, j, count) + bfs(i, j+1, count) + bfs(i, j-1, count)
            return count
        return bfs(0, 0, 0)

    def digit_add(self, n1, n2):
        s = str(n1) + str(n2)
        res = 0
        for d in s:
            res += int(d)
        return res

print(Solution().movingCount(3, 1, 0))