# A circus is designing a tower routine consisting of people standing atop one anoth­er's shoulders.
# Each person must be both shorter and lighter than the person below him or her.
# Given the heights and weights of each person in the circus,
# write a method to compute the largest possible number of people in such a tower.
#
# Example:
#       Input: height = [65,70,56,75,60,68]   weight = [100,150,90,190,95,110]
#       Output: 6
# Explanation: The longest tower is length 6 and includes from top to bottom:
#               (56,90), (60,95), (65,100), (68,110), (70,150), (75,190)


class Solution:
    def __init__(self):
        self.res = []

    def bestSeqAtIndex(self, height, weight):
        pair = []
        for h, w in zip(height, weight):
            pair.append((h, w))
        pair = sorted(pair)
        res = 1 + self.check_be_top(pair, len(pair)-2, len(pair)-1)
        for i in self.res:
            print(i)
        return res

    def check_be_top(self, pair, top_index, this_index):
        print(top_index)
        if top_index < 0:
            return 0
        top = pair[top_index]
        this = pair[this_index]
        if self.res and (this[0] >= self.res[-1][0][0] or this[1] >= self.res[-1][0][1]):
            return self.check_be_top(pair, top_index-2, this)

        if top[0] < this[0] and top[1] < this[1]:
            self.res.append((top, this))
            return 1 + self.check_be_top(pair, top_index-1, top_index)
        else:
            # res = max(self.check_be_top(pair, top_index - 1, top_index),
            #           self.check_be_top(pair, top_index - 1, this_index))
            res = self.check_be_top(pair, top_index - 1, top_index)
            # res = self.check_be_top(pair, top_index - 1, this_index)
            return res


height = [65,70,56,75,60,68]
weight = [100,150,90,190,95,110]
print(Solution().bestSeqAtIndex(height, weight), 6)


height = [10,20,41,40,50]
weight = [1,2,2,3,6]
print(Solution().bestSeqAtIndex(height, weight), 5)


# (1306, 1651) @-
# (1356, 7985)
# (2868, 5042)
# (4941, 428)  @-
# (5485, 3995) @
# (6017, 5991) @
# (6181, 8594) @
# (6331, 7561)
# (7535, 9391) @
# (8941, 7036)
height = [2868,5485,1356,1306,6017,8941,7535,4941,6331,6181]
weight = [5042,3995,7985,1651,5991,7036,9391,428,7561,8594]
print(Solution().bestSeqAtIndex(height, weight), 5)
