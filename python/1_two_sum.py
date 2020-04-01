# Given an array of integers, return indices of the two numbers such that they add up to a s
# pecific target.
#
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
#
# Example:
#   Given nums = [2, 7, 11, 15], target = 9,
#
#   Because nums[0] + nums[1] = 2 + 7 = 9,
#   return [0, 1].


class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        p_start = 0
        p_end = len(nums) - 1

        while p_start < p_end:
            for p in range(p_start, p_end):
                if nums[p] + nums[p_end] == target:
                    return [p, p_end]
                else:
                    continue
            p_end -= 1

        return [None, None]


if __name__ == "__main__":
    nums = [-1,-2,-3,-4,-5]
    target = -8
    r = Solution().twoSum(nums, target)
    print(r)
