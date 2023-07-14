# def maxOperations( nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: int
#     """

#     total_op = 0

#     for num in nums:
#         find = k - num
#         print(find, num, nums)
#         if find in nums:
#             nums.remove(find)
#             nums.remove(num)
#             total_op += 1
#     return total_op

# print(maxOperations([3,1,3,4,3], 6))


from collections import Counter
def maxOperations(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    total_op = 0

    counter = Counter(nums)

    for num in nums:
        temp = k - num
        print("num ", num, "temp ", temp)
        print(counter)
        # check if there are more than 2 of same number
        if temp == num and counter[num] >= 2:
            print("inif")
            counter[num] -= 2
            total_op += 1

        # check if both temp and num in counter
        elif temp != num and temp in counter and counter[temp] >= 1 and counter[num] >= 1:
            print("inelif")
            counter[temp] -= 1
            counter[num] -= 1
            total_op += 1

    return total_op

print(maxOperations([4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4], 2))