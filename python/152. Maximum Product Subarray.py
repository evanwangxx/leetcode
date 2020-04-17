# Given an integer array nums,
# find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# Example 1:
#       Input: [2,3,-2,4]
#       Output: 6
#       Explanation: [2,3] has the largest product 6.
# Example 2:
#       Input: [-2,0,-1]
#       Output: 0
#       Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


class Solution:
    def maxProduct(self, nums):
        if not nums:
            return None
        nmax = nums[0]
        imax = nums[0]
        imin = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax
            imax = max(imax * nums[i], nums[i])
            imin = min(imin * nums[i], nums[i])
            nmax = max(nmax, imax)
        return nmax


test = [2,3,-2,4]
print(Solution().maxProduct(test))

test = [-2,0,-1]
print(Solution().maxProduct(test))

test = [-2,3,-4]
print(Solution().maxProduct(test))