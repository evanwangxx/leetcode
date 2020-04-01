class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        x1 = y1 = 0
        x2 = len(matrix)-1
        y2 = len(matrix[0]) - 1
        if x1 == x2:
            return matrix[0]
        if y1 == y2:
            return [i[0] for i in matrix]

        res = []
        while x1 <= x2 and y1 <= y2:
            sin = self.spiralSingle(x1, y1, x2, y2, matrix)
            res.extend(sin)
            x1 += 1
            y1 += 1
            x2 -= 1
            y2 -= 1
            if x1 == x2:
                res.extend(matrix[x1][y1:y2+1])
                break
            if y1 == y2:
                tmp = [matrix[x][y1] for x in range(x1, x2+1)]
                res.extend(tmp)
                break
        return res

    def spiralSingle(self, x1, y1, x2, y2, matrix):
        i = x1
        j = y1
        res = []
        while x1 <= i <= x2 and y1 <= j <= y2:
            res.append(matrix[i][j])

            if i == x1 + 1 and j == y1:
                return res
            if i == x1 and j != y2:
                j += 1
            elif i != x2 and j == y2:
                i += 1
            elif i == x2 and j != y1:
                j -= 1
            elif i != x1 and j == y1:
                i -= 1



m = [[1,2,3,4],
     [10,11,12,5],
     [9,8,7,6]]
print(Solution().spiralOrder(m))

m = [[1,2,3],
     [8,9,4],
     [7,6,5]]
print(Solution().spiralOrder(m))

m = [[1,2,3],
     [10,11,4],
     [9,12,5],
     [8,7,6]]
print(Solution().spiralOrder(m))

m = [[1,2,3]]
print(Solution().spiralOrder(m))

m = [[1],[2],[3]]
print(Solution().spiralOrder(m))

m = [[1,2,3,4,5],
     [10,9,8,7,6]]
print(Solution().spiralOrder(m))