def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    if len(nums) == 1:
        return nums

    n = len(nums)

    i = 0

    for j in range(n):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

# store zero to be replaced in i
# find next place that does not have zero in j