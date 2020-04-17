# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
# Example:
#       Input: [10,9,2,5,3,7,101,18]
#       Output: 4
#       Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Note:
#       1. There may be more than one LIS combination, it is only necessary for you to return the length.
#       2. Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?


class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0

        res = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    res[i] = max(res[j]+1, res[i])

        return max(res)


x = [10,9,2,5,3,7,101,18]
print(Solution().lengthOfLIS(x))
