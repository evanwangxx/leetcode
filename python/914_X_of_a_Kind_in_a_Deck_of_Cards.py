# In a deck of cards, each card has an integer written on it.
# Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards,
# where: Each group has exactly X cards.
# All the cards in each group have the same integer.
#  
# Example 1:
#       Input: deck = [1,2,3,4,4,3,2,1]
#       Output: true
#       Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
# Example 2:
#       Input: deck = [1,1,1,2,2,2,3,3]
#       Output: false´
#       Explanation: No possible partition.
# Example 3:
#       Input: deck = [1]
#       Output: false
#       Explanation: No possible partition.
# Example 4:
#       Input: deck = [1,1]
#       Output: true
#       Explanation: Possible partition [1,1].
# Example 5:
#       Input: deck = [1,1,2,2,2,2]
#       Output: true
#       Explanation: Possible partition [1,1],[2,2],[2,2].

import math
class Solution:
    def hasGroupsSizeX(self, deck):
        dic = {}
        for i in deck:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1

        gcd = None
        for v in dic.values():
            gcd = math.gcd(v, gcd) if gcd else v
            if gcd < 2:
                return False
        return True


x = [1,2,3,4,4,3,2,1]
print(Solution().hasGroupsSizeX(x))

x = [1,1,1,2,2,2,3,3]
print(Solution().hasGroupsSizeX(x))

x = [1]
print(Solution().hasGroupsSizeX(x))

x = [1,1]
print(Solution().hasGroupsSizeX(x))

x = [1,1,1,1,2,2,2,2,2,2]
print(Solution().hasGroupsSizeX(x))
