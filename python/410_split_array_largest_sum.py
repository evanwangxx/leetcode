# Given an array which consists of non-negative integers and an integer m,
# you can split the array into m non-empty continuous subarrays.
# Write an algorithm to minimize the largest sum among these m subarrays.
#
# Note: If n is the length of array, assume the following constraints are satisfied:
#       1 ≤ n ≤ 1000
#       1 ≤ m ≤ min(50, n)
#
# Examples:
#   Input:
#       nums = [7,2,5,10,8]
#       m = 2
#   Output:
#       18
#
# Explanation:
#   There are four ways to split nums into two subarrays.
#   The best way is to split it into [7,2,5] and [10,8],
#   where the largest sum among the two subarrays is only 18.

MAX_ITERATION = 10
class Solution:
    def splitArray(self, nums: [int], m: int) -> int:
        max_sum = sum(nums)
        min_sum = max(nums)

        index = 0
        while min_sum < max_sum and index < MAX_ITERATION:
            mid_sum = (max_sum + min_sum) / 2
            cnt = 1
            temp_sum = 0
            for n in nums:
                temp_sum += n
                if temp_sum > mid_sum:
                    temp_sum = n
                    cnt += 1
            if cnt > m:
                min_sum = mid_sum + 1
            else:
                max_sum = mid_sum

            index += 1
            print(min_sum, mid_sum, max_sum, cnt)

        return min_sum


class Solution2(object):
    def splitArray(self, nums, m):
        # binary search for min_max
        left, right = sum(nums) / m, sum(nums)
        while left <= right:
            mid = right - ((right - left) >> 1)
            if self.valid_max(nums, m, mid) and (not self.valid_max(nums, m, mid - 1)):
                return mid
            else:
                if not self.valid_max(nums, m, mid):
                    left = mid + 1
                else:
                    right = mid - 1

        return right

    def valid_max(self, nums, k, max):
        n = len(nums)
        div = 1
        sum = nums[0]
        for i in range(1, n):
            if sum > max:
                return False
            if sum + nums[i] > max:
                div += 1
                sum = nums[i]
            else:
                sum += nums[i]
        # note that we have to ensure sum <= max
        return (sum <= max) and (div <= k)

if __name__ == "__main__":
    x1 = [7,2,5,10,8]
    print(Solution().splitArray(x1, 2))
