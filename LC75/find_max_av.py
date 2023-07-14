def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """

    if len(nums) == 1:
        return nums[0] / float(k)

    len_n = len(nums)
    max_av = 0


    for i in range(len(nums)-k + 1):
        sums = sum(nums[i:i+k])
        print(sums)
        av = sums / float(k)
        print(av)
        max_av = max(max_av, av)

    return max_av

print(findMaxAverage([1,12,-5,-6,50,3], 4))