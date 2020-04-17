# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#   (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
# You are given a target value to search. If found in the array return true, otherwise return false.
#
# Example 1:
#       Input: nums = [2,5,6,0,0,1,2], target = 0
#       Output: true
# Example 2:
#       Input: nums = [2,5,6,0,0,1,2], target = 3
#       Output: false
# Follow up:
#       This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
#       Would this affect the run-time complexity? How and why?



class Solution:
    def search(self, nums, target):
        if not nums:
            return False

        min_index = self.find_min(nums)
        if target == nums[min_index]:
            return True
        elif nums[0] <= target <= nums[min_index-1] and min_index != 0:
            return self.find_target(nums[:min_index-1], target)
        elif nums[min_index] <= target <= nums[-1]:
            return self.find_target(nums[min_index:], target)

    def find_min(self, nums):
        if nums[0] < nums[-1]:
            return 0

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] > nums[mid + 1]:
                return mid + 1

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] < nums[right]:
                right = mid
        return left

    def find_target(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return False

test = [2,5,6,0,0,1,2]
print(Solution().search(test, 0), True)

test = [2,5,6,0,0,1,2]
print(Solution().search(test, 3), False)

test = [1,3]
print(Solution().search(test, 3), True)

test = [3,1]
print(Solution().search(test, 3), True)

test = [1]
print(Solution().search(test, 2), False)