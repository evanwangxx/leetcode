# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example 1:
#   Input: [3,2,3]
#   Output: 3
#
# Example 2:
#   Input: [2,2,1,1,1,2,2]
#   Output: 2


class Solution:
    def majorityElement(self, nums):
        current = nums[0]
        count = 1

        for n in nums[1:]:
            if n != current:
                count -= 1
            else:
                count += 1

            if count < 0:
                current = n
                count = 1

        return current


x1 = [47,47,72,47,72,47,79,47,12,92,13,47,47,83,33,15,18,47,47,47,47,64,47,65,47,47,47,47,70,47,47,55,47,15,60,47,47,47,47,47,46,30,58,59,47,47,47,47,47,90,64,37,20,47,100,84,47,47,47,47,47,89,47,36,47,60,47,18,47,34,47,47,47,47,47,22,47,54,30,11,47,47,86,47,55,40,49,34,19,67,16,47,36,47,41,19,80,47,47,27]
x2 = [3,3,4]
s = Solution()
print(s.majorityElement(x1), s.majorityElement(x2))