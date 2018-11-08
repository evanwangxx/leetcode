# 283. Move Zeroes

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    z = 0
    nz = z + 1
    for i in range(0, len(nums) - 1):
        if nums[i] == 0:
            z = i
            nz = z + 1

            while nums[nz] == 0:
                if nz <= len(nums) - 2:
                    nz += 1
                else:
                    break
            nums[i] = nums[nz]
            nums[nz] = 0

    return nums

x = [0,1,0,3,12]
print(moveZeroes(x))
