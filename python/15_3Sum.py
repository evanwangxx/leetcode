# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
#
# Note: The solution set must not contain duplicate triplets.
# Example: Given array nums = [-1, 0, 1, 2, -1, -4],
#          A solution set is:
#            [
#                [-1, 0, 1],
#                [-1, -1, 2]
#            ]


class Solution:
    def threeSumHelper(self, nums, target):
        rl = []
        for i in range(len(nums)-1):
            x = nums[i]
            for j in range(i+1, len(nums)):
                y = nums[j]
                if x + y == target:
                    rl.append([x, y])
                    continue
                elif x + y > target:
                    continue
        return rl

    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()
        rl = []
        for i in range(2, len(nums)):
            this_value = nums[i]
            next_value = nums[i + 1] if i < len(nums) - 1 else None
            if this_value < 0 or (next_value and this_value == next_value):
                continue
            else:
                for tmp in self.threeSumHelper(nums[:i], -this_value):
                    tmp.append(this_value)
                    if tmp not in rl:
                        rl.append(tmp)
        return rl


if __name__ == "__main__":
    x = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    rll = s.threeSum(x)
    print(rll)
