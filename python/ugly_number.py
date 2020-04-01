class Solution:
    def nthUglyNumber(self, n):
        p2 = p3 = p5 = 0
        res = [0 for _ in range(n)]
        res[0] = 1

        for i in range(1, n):
            ugly = min(res[p2]*2, res[p3]*3, res[p5]*5)
            res[i] = ugly
            if ugly == res[p2]*2:
                p2 += 1
            if ugly == res[p3]*3:
                p3 += 1
            if ugly == res[p5]*5:
                p5 += 1
        print(res)
        return res[-1]

    def nth_ugly_number(self, n):
        res = [0 for _ in range(n)]
        res[0] = 1
        p2 = p3 = p5 = 0

        count = 1
        while count < n:
            res[count] = min(res[p2]*2, res[p3]*3, res[p5]*5)
            if res[count] == res[p2]*2:
                p2 += 1
            if res[count] == res[p3]*3:
                p3 += 1
            if res[count] == res[p5]*5:
                p5 += 1
            count += 1
        print(res)
        return res[-1]


print(Solution().nthUglyNumber(10), Solution().nth_ugly_number(10))

