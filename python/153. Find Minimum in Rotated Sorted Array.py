# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#   (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# Find the minimum element.

# You may assume no duplicate exists in the array.
#
# Example 1:
#       Input: [3,4,5,1,2]
#       Output: 1
# Example 2:
#       Input: [4,5,6,7,0,1,2]
#       Output: 0


class Solution:
    def findMin(self, nums):
        if not nums:
            return None
        if nums[0] < nums[-1]:
            return nums[0]

        i = 0
        j = len(nums) - 1
        while i < j:
            mid = int((i + j) / 2)
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] >= nums[i]:
                i = mid + 1
            elif nums[mid] <= nums[j]:
                j = mid
        return nums[i]

test = [3,4,5,1,2]
print(Solution().findMin(test))

test = [4,5,6,7,0,1,2]
print(Solution().findMin(test))

test = [0,1,2]
print(Solution().findMin(test))
