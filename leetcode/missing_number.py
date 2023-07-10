def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    sort = sorted(nums)

    if sort[0] == 1:
        return 0

    for i, num in enumerate(sort):
        if i == len(sort) - 1:
            return sort[i] + 1

        next = num + 1

        if next == sort[i+1]:
            continue
        else:
            return next