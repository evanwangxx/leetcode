class Solution:
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""

        n1 = len(str1)
        n2 = len(str2)
        if n1 < n2:
            n1, n2 = n2, n1
        while n2 != 0:
            n1, n2 = n2, n1 % n2
        return str1[:n1]


# x1 = "asasas"
# x2 = "qweqwe"

x1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
x2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"

print(Solution().gcdOfStrings(x1, x2))
