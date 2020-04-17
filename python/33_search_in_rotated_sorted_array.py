# Search in Rotated Sorted Array
#
# Ex: [4, 5, 6, 7, 0, 1, 2], target = 0
#     return 4


# class Solusion:
#     MAX_ITER = 20
#
#     def bisection_find_min(self, nums):
#         l = 0
#         r = len(nums) - 1
#         i = 0
#         while l < r:
#             i = int((l + r) / 2)
#             value = nums[i]
#             if value < nums[r]:
#                 r = i
#             elif value > nums[l]:
#                 l = i + 1
#         return i, nums[i]
#
#     def bisection(self, nums, target):
#         if not nums or target < nums[0]:
#             return -1
#         l = 0
#         r = len(nums) - 1
#         return self.bisection_helper(nums, l, r, target)
#
#     def bisection_helper(self, nums, l, r, target):
#         if l > r:
#             return -1
#         i = int((l + r) / 2)
#         if nums[i] == target:
#             return i
#         elif nums[i] < target:
#             return self.bisection_helper(nums, i + 1, r, target)
#         elif nums[i] > target:
#             return self.bisection_helper(nums, l, i, target)
#
#     def search(self, nums, target) -> int:
#         if not nums:
#             return -1
#         min_index, min_value = self.bisection_find_min(nums)
#         if nums[0] < target <= nums[min_index - 1]:
#             return self.bisection(nums[0: min_index - 1], target)
#         else:
#             value = self.bisection(nums[min_index:], target)
#             return min_index + value if value != -1 else -1


class Solution:
    def search(self, nums, target):
        if not nums:
            return -1

        min_index = self.find_min(nums)
        if target == nums[min_index]:
            return min_index
        elif target > nums[-1]:
            return self.find_target(nums[:min_index], target)
        elif target <= nums[-1]:
            index = self.find_target(nums[min_index:], target)
            return min_index + index if index != -1 else -1

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
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1


test = [4, 5, 6, 7, 0, 1, 2]
print(Solution().search(test, 7), 3)

test = [4, 5, 6, 7, 0, 1, 2]
print(Solution().search(test, 3), -1)

test = [1, 3]
print(Solution().search(test, 3), 1)

test = [3, 1]
print(Solution().search(test, 3), 0)

test = [3, 1]
print(Solution().search(test, 0), -1)

test = [5, 1, 3]
print(Solution().search(test, 3), 2)
