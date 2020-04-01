# Given a triangle, find the minimum path sum from top to bottom.
# Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note: Bonus point if you are able to do this using only O(n) extra space,
#       where n is the total number of rows in the triangle.


class Solution:
    def minimumTotal(self, triangle):
        i = len(triangle) - 1
        res = []
        for j in range(len(triangle[-1])):
            res.append(self.dp_up_search(i, j, triangle, {}))
        return min(res)

    def dp_up_search(self, i, j, tri, dict):
        k = str(i) + "-" + str(j)
        if k in dict.keys():
            return dict[k]

        if i == 0:
            dict[k] = tri[0][0]
        elif j == 0:
            dict[k] = self.dp_up_search(i-1, j, tri, dict) + tri[i][j]
        elif j == len(tri[i])-1:
            dict[k] = self.dp_up_search(i-1, len(tri[i-1])-1, tri, dict) + tri[i][j]
        else:
            dict[k] = min(self.dp_up_search(i-1, j-1, tri, dict), self.dp_up_search(i-1, j, tri, dict)) + tri[i][j]
        return dict[k]


x = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
    ]
print(Solution().minimumTotal(x))