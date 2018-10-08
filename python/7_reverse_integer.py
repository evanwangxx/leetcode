class Solution:

    @staticmethod
    def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        reverse = 0
        sign = [1, -1][x < 0]

        if x < 0:
            x = x * sign

        while x != 0:
            digit = x % 10
            x = int(x / 10)
            reverse = reverse * 10 + digit

        reverse = reverse * sign

        if reverse <= -2**31 or reverse >= 2**31-1:
            return 0

        return reverse



if __name__ == "__main__":
    test = Solution.reverse(1534236469)
    print(0, test)

    test = Solution.reverse(123)
    print(321, test)

    test = Solution.reverse(-123)
    print(-321, test)