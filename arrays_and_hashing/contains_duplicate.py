# Given an integer array nums, return true if any value
# appears at least twice in the array, and return false
# if every element is distinct.

# true if 2x
# false if nothing repeated
# [1,2,3]

# my attempt
def containsDuplicate(nums):
    counter = {}

    for num in nums:
        if num in counter:
            return True
        else:
            counter[num] = 1

    return False

print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

# neetcode solution
def containsDuplicate2(nums: List[int]) -> bool:
    hashset = set()

    for n in nums:
        if n in haset:
            return True
        hashset.add(n)
    return false