# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#   (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
# The array may contain duplicates.
#
# Example 1:
#       Input: [1,3,5]
#       Output: 1
# Example 2:
#       Input: [2,2,2,0,1]
#       Output: 0
# Note:
#       This is a follow up problem to Find Minimum in Rotated Sorted Array.
#       Would allow duplicates affect the run-time complexity? How and why?

class Solution:
    def findMin(self, nums):
        if not nums:
            return None
        if nums[0] < nums[-1]:
            return nums[0]

        left = 0
        right = len(nums)-1
        while left < right:

            mid = int((left + right) / 2)
            if nums[mid] > nums[mid + 1]:
                return nums[mid+1]

            if nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
        return nums[left]

test = [1,3,5]
print(Solution().findMin(test))

test = [2,0,1]
print(Solution().findMin(test))

test = [2,2,2,0,1]
print(Solution().findMin(test))

test = [2,0,1,1,1,1]
print(Solution().findMin(test))

test = [3,1,3]
print(Solution().findMin(test))