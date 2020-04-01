# A popular masseuse receives a sequence of back-to-back appointment requests and is debating which ones to accept.
# She needs a break between appointments and therefore she cannot accept any adjacent requests.
# Given a sequence of back-to-back appoint­ ment requests,
# find the optimal (highest total booked minutes) set the masseuse can honor. Return the number of minutes.
#
# Note: This problem is slightly different from the original one in the book.
#
# Example 1:
#       Input:  [1,2,3,1]
#       Output:  4
#       Explanation:  Accept request 1 and 3, total minutes = 1 + 3 = 4
# Example 2:
#       Input:  [2,7,9,3,1]
#       Output:  12
#       Explanation:  Accept request 1, 3 and 5, total minutes = 2 + 9 + 1 = 12
# Example 3:
#       Input:  [2,1,4,5,3,1,1,3]
#       Output:  12
#       Explanation:  Accept request 1, 3, 5 and 8, total minutes = 2 + 4 + 3 + 3 = 12


class Solution:
    def __init__(self):
        self.res = None

    def massage(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        self.res = [0 for _ in nums]
        self.dp(len(self.res)-1, nums)
        return self.res[-1]

    def pointer(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        res = [0 for _ in nums]
        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])
        i = 2
        while i < len(res):
            res[i] = max(res[i-1],  res[i-2] + nums[i])
            i += 1
        return res[-1]

    def dp(self, i, nums):
        if i == 0:
            self.res[i] = nums[0]
        elif i == 1:
            self.res[i] = max(nums[0], nums[1])
        else:
            self.res[i] = max(self.dp(i-1, nums), self.dp(i-2, nums) + nums[i])
        return self.res[i]


x = [1,2,3,1]
print(Solution().massage(x))

x = [2,7,9,3,1]
print(Solution().massage(x))

x = [2,1,4,5,3,1,1,3]
print(Solution().massage(x))
