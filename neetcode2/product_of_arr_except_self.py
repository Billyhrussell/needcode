def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    n = len(nums)

    left = [1] * n
    right = [1] * n

    # 1, 2, 3
    # RANGE ends before n
    # aka range = 1, 2, 3
    # start at 1
    for i in range(1,n):
        left[i] = left[i-1] * nums[i - 1]
        # left[1] = left[0] * nums[0]
        #         = [1]     * 1
        # left[2] = left[1] * nums[1]
        #         = 1       *    2
        # left[3] = left[2] * nums[2]
        #         = 2    *       3

    #  2 , 1, 0
    # start at 2nd from end
    for i in range(n-2, -1, -1):
        print(i)
        right[i] = right[i+1] * nums[i+1]
        # right[2] = right[3] * nums[3]
        # right[2] =     1    *   4
        # right[1] = right[2] * nums[2]
        # right[1] =   4      *    3
        # right[0] = right[1] * nums[1]
        # right[0] =    12    *  2

    # left = [1, 1, 2, 6]
    # right= [24, 12, 4, 1]
    result = [left[i] * right[i] for i in range(n)]

    return result

nums = [1,2,3,4]
print(productExceptSelf(nums))