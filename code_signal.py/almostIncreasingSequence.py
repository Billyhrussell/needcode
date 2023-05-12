
# input: int arr (sequence)
# determine if possible to obtain strictly increasaing sequence
# by removing no more than 1 elem from arr
# output: t/f

# ex: [1, 3, 2, 1]
# false

# ex: 1, 3, 3
# true

#  1 2 3 2 4
# def solution(sequence):
#     skips = 0
#     prev = sequence[0]
#     sq_length = len(sequence)

#     for i, num in enumerate(sequence[1::]):
#         if prev >= num:
#             # 4 > 99
#             skips += 1
#             if num < sequence[i]:
#                 # 3 < 2
#                 prev = num
#                 # prev = 3
#                 print("prev" , prev)
#         else:
#             print("in else ")
#             print(num)
#             print(sequence[i])
#             if prev < sequence[i]:
#                 # 99 < 5
#                 print("in if")
#                 prev = num


#     print("skips " ,skips)
#     if skips > 1:
#         return False

#     return True

# print(solution([1, 2, 3, 4, 99, 5, 6]))




# def solution(sequence):

#     skips = 0
#     prev = sequence[0]
#     print(len(sequence))

#     for i, num in enumerate(sequence[1::]):
#         print("i", i)
#         if(prev < num):
#             if num < sequence[i+1]:
#                 prev = num
#             elif i == (len(sequence) -1):
#                 break
#             else:
#                 print("in first skip")
#                 skips += 1
#         else:
#             print("in else skip")
#             skips += 1

#     print(skips)

#     if skips > 1:
#         return False

#     return True

# print(solution([1, 2, 3, 4, 99, 5, 6]))
# print(solution([1, 3, 2, 1]))
# print(solution([1, 3, 2]))



# 3 1 2 3
#  true

# 1 3 2 3
#  true

class Solution:
    def canBeIncreasing(self, nums):
        indx = -1
        count = 0
        n = len(nums)

        # count the number of non-increasing elements
        for i in range(n-1):
            if nums[i] >= nums[i+1]:
                indx = i
                count += 1

        #the cases explained above
        if count==0:
            return True

        if count == 1:
            if indx == 0 or indx == n-2:
                return True
            if nums[indx-1] < nums[indx+1] or(indx+2 < n and nums[indx] < nums[indx+2]):
                return True

        return False