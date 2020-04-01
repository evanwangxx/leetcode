# 0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。
# 求出这个圆圈里剩下的最后一个数字。
#
# 例如，0、1、2、3、4这5个数字组成一个圆圈，
# 从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。


class Solution:
    def lastRemaining(self, n, m):
        remains = [i for i in range(n)]
        start = 0
        while len(remains) != 1:
            start, remains = self.kill_kth_person(start, m, remains)
        return remains[0]

    def kill_kth_person(self, start, k, remains):
        count = 1
        while count < k:
            start += 1
            count += 1
            if start >= len(remains):
                start = 0
        remains.pop(start)
        if start >= len(remains):
            start = 0
        return start, remains


class Solution2:
    def lastRemaining(self, n: int, m: int) -> int:
        last = 0
        for i in range(2, n + 1):
            last = (last + m) % i
        return last


print(Solution().lastRemaining(5, 3), Solution2().lastRemaining(5, 3))
print(Solution().lastRemaining(10, 2), Solution2().lastRemaining(10, 2))
print(Solution().lastRemaining(10, 3), Solution2().lastRemaining(10, 3))
print(Solution().lastRemaining(10, 7), Solution2().lastRemaining(10, 7))

