# input: nums (int arr ) sorted in inc order
# remove duplicates so elem appears only once
# order of elems should stay same
#

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    k = []

    for num in nums:
        if num in k:
            continue
        else:
            k.append(num)

    return len(k)


print(removeDuplicates([1,1,2]))
