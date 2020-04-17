class Solution:
    def myPow(self, x, n):
        if n < 0:
            n = -n
            x = 1 / x
        return self.fast_power(x, n)

    def fast_power(self, x, n):
        if n == 0:
            return 1.0

        half_pow = self.myPow(x, int(n / 2))
        is_even = (n % 2 == 0)

        if is_even:
            return half_pow * half_pow
        else:
            return half_pow * half_pow * x


print(Solution().myPow(-2, 2))