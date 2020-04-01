class Solution:
    def missingNumber(self, nums):
        return self.method2(nums)

    def method1(self, nums):
        if not nums:
            return 0

        for i in range(len(nums)):
            if abs(nums[i]) >= len(nums):
                continue
            nums[abs(nums[i])] *= -1
            # if nums[i] == 0:
            #     nums[i] = 1
            # print(i, nums)

        for i in range(len(nums)):
            if nums[i] > 0:
                return i
        return len(nums)

    def method2(self, nums):
        total_sum = sum(nums)
        the_sum = ((0+len(nums)) * (len(nums)+1))/2

        return int(abs(the_sum - total_sum))

x = [3,0,1]
print(Solution().missingNumber(x), 2)

x = [9,6,4,2,3,5,7,0,1]
print(Solution().missingNumber(x), 8)

x = [0]
print(Solution().missingNumber(x), 1)

x = [1]
print(Solution().missingNumber(x), 0)

x = [2, 0]
print(Solution().missingNumber(x), 1)