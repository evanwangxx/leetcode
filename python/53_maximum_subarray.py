# Given an integer array nums, find the contiguous subarray (containing at least
# one number) which has the largest sum and return its sum.
#
# Example:
#   Input: [-2,1,-3,4,-1,2,1,-5,4],
#   Output: 6
#   Explanation: [4,-1,2,1] has the largest sum = 6.
#
# Follow up:
#   If you have figured out the O(n) solution, try coding another solution
#   using the divide and conquer approach, which is more subtle.


class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0

        max_sum = nums[0]
        current = nums[0]

        for n in nums[1:]:
            if current >= 0:
                current += n
            else:
                current = n
            max_sum = max(current, max_sum)
        return max_sum


x = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(x))
