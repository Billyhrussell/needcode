

# # return sum(c in "aeiou" for c in sentence)

# sentence = "Hello"
# for(let i = 0; i < sentence.length; i+=2){ # i = 0
#     print(sentence[i])
# }

# # h
# # l
# # o


# for c in sentence
# "h"
# "e"
# "l"
# "l"
# "o"

# # what you're searching IN
# if "h" in sentence:
#     print True

# # Already known* Given a string of words, return the length of the shortest word(s).
# # Example: "Let's travel abroad shall we"
# # Output: 2
# # Initial Solution:

# # for is the stepping from one elem to next
# # li = ["lets", "travel", "abroad", "shall", "we"]

# def find_short(s):
#     x = s.split()
#     return len(min(x, key=len))
# Better Solution:
# def find_short(s):
#     return min(len(x) for x in s.split())

# class Solution(object):
#     def containsDuplicate(self,nums):
#         x = max(list(nums), key = nums.count)
#         print(x)
#         if x > 1:
#             return True
#         return False

# nums = [1,2,3,2,2,2,2,2]
# solution = Solution()
# print(solution.containsDuplicate(nums))

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """

#         nums_copy = list(nums)
#         nums_sum = []
#         ans = []

#         while len(nums_sum) != 2:
#             first_num = nums_copy[0]
#             nums_copy.pop(0)

#             print("FIRST_NUM ", first_num)
#             print("NUMS_COPY ", nums_copy)

#             for num in nums_copy:
#                 if num + first_num == target:
#                     nums_sum.append(num)
#                     nums_sum.append(first_num)

#         print(nums_sum)

#         for i, n in enumerate(nums):
#             if n == nums_sum[0] or n == nums_sum[1]:
#                 ans.append(i)
#         return ans

# nums = [3,2,4]
# target = 6

# solution = Solution()
# print(solution.twoSum(nums,target))


# def number_to_pwr(number, p):
#     answer = number
#     for index in range(p):
#         print("INDEX ", index)
#         answer *= number
#     return answer

# print(number_to_pwr(10,4))

# p = {'q': 1, 'r':2}
# q = {'q': 1}

# print(p == q)

# print(ord('t'))
# print(ord('a'))
# count = [0] * 26
# print(count)
# r = range(4)
# for x in r:
#     print(x)

# # print(range(4))

# correct_order = ["(", ")", "[", "]", "{", "}"]

# print(correct_order[1])

stack = [1]


if not stack:
    print("not stack")
if stack:
    print("yes stack")

# print(stack[-1])