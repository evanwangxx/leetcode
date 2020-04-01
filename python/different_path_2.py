# 输入: [ [0,0,0],
#         [0,1,0],
#         [0,0,0] ]
#   输出: 2
#   解释: 3x3 网格的正中间有一个障碍物。
#         从左上角到右下角一共有 2 条不同的路径：
#           1. 向右 -> 向右 -> 向下 -> 向下
#           2. 向下 -> 向下 -> 向右 -> 向右

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        return self.dp_path(len(obstacleGrid)-1, len(obstacleGrid[0])-1, obstacleGrid, {})

    def dp_path(self, x, y, grid, dic):
        k = str(x) + "|" + str(y)
        if k in dic.keys():
            return dic[k]

        if x == 0 and y == 0:
            dic[k] = 1 if grid[x][y] != 1 else 0
            return dic[k]
        elif x == 0 and y != 0:
            dic[k] = self.dp_path(x, y-1, grid, dic) if grid[x][y] != 1 else 0
            return dic[k]
        elif x != 0 and y == 0:
            dic[k] = self.dp_path(x-1, y, grid, dic) if grid[x][y] != 1 else 0
            return dic[k]

        if grid[x][y] == 1:
            dic[k] = 0
        else:
            dic[k] = self.dp_path(x-1, y, grid, dic) + self.dp_path(x, y-1, grid, dic)
        return dic[k]


x = [ [0,0,0],[0,1,0],[0,0,0] ]
print(Solution().uniquePathsWithObstacles(x))

x = [ [0, 1]]
print(Solution().uniquePathsWithObstacles(x))