class Solution:
    def countDigitOne(self, n: int):
        count = 0
        for i in range(n):
            if i < 10 and i % 10 == 1:
                count += 1
            elif i // 10 % 10== 1:
                count += 1


Solution().countDigitOne(10)
print(101 // 10 % 10)