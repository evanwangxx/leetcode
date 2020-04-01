# 输入一个整型数组，数组里有正数也有负数,数组中的一个或连续多个整数组成一个子数组。
# 求所有子数组的和的最大值。要求时间复杂度为O(n)。
#
# 示例:
#       输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
#       输出: 6
#       解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。


class Solution:
    def maxSubArray2(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] <= 0:
                i += 1
            else:
                break
        if i == len(nums):
            i = 0
        nums = nums[i:]
        max_sum = nums[0]
        tmp_sum = nums[0]

        for i in range(1, len(nums)):
            if tmp_sum + nums[i] <= 0:
                tmp_sum = max(min(tmp_sum, 0), nums[i])
            else:
                tmp_sum += nums[i]
            max_sum = max(max_sum, tmp_sum)

        max_sum = max(max_sum, tmp_sum)
        return max_sum

    def maxSubArray(self, nums):
        if not nums:
            return 0
        max_sum = max(nums)
        if max_sum <= 0:
            return max_sum

        tmp_sum = 0
        for i in range(0, len(nums)):
            tmp_sum += nums[i]
            if tmp_sum < 0:
                tmp_sum = 0
                continue
            else:
                max_sum = max(tmp_sum, max_sum)
        return max_sum


x = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(x), 6)

x = [-2,1]
print(Solution().maxSubArray(x), 1)

x = [-2,-1]
print(Solution().maxSubArray(x), -1)

x = [-2,3,1,3]
print(Solution().maxSubArray(x), 7)