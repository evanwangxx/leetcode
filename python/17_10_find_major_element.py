# A majority element is an element that makes up more than half of the items in an array.
# Given a positive integers array, find the majority element.
# If there is no majority element, return -1.
# Do this in O(N) time and O(1) space.
#
# Example 1:
#   Input: [1,2,5,9,5,9,5,5,5]
#   Output: 5
#  
# Example 2:
#   Input: [3,2]
#   Output: -1


class Solution:
    def majorityElement(self, nums):
        if not nums:
            return -1

        count = 1
        pre = nums[0]
        for n in nums[1:]:
            if n == pre:
                count += 1
            else:
                count -= 1
            if count < 0:
                pre = n
                count = 1
        # print(pre, count)
        return pre if count > 0 else -1


x = [6,5,5]
print(Solution().majorityElement(x))