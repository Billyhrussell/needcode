

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
# r = range(2, 2)
# for x in r:
#     print(x)

# # print(range(4))

# correct_order = ["(", ")", "[", "]", "{", "}"]

# print(correct_order[1])

# stack = [1]


# if not stack:
#     print("not stack")
# if stack:
#     print("yes stack")

# # print(stack[-1])


# for i in range(9)[::2]:
#     print(i)

# ans = ['abc', 'abc', 'c']
# # print(max(ans))
# print(len("abc"))

# str = "hzanvi"

# print(str.split("a"))

# arr = [1, 2, 3]
# print(arr[-1])

# str = 'AAABBBABAB'
# print(str.split('A'))
# print(str.split('B'))

# a = str.split('A')

# print(len(max(a, key=len)))


# string = "string"
# print(len(string))

# dp = [0] * len(string)
# print(dp)

# print(string[6])


# for i in range(3):
#     print(i)

# events = [[1,2],[2,3],[3,4],[1,2]]
# events.sort()
# print(events)


# t = {"a" : 1,
#      "b" : 1}
# s = {"b" : 1,
#      "a" : 1}

# if s == t:
#     print(True)

# print(ord("a"))

# print(ord("b"))

# print(ord("b") - ord("a"))

ans = [""] * 3

str = "  hello there   "

# ls = list(str)

# ls = str.split()

# print(ls)

# nums = [1,2,3]
# zs = [0, 0]

# # print(nums.append(zs))
# nums.append(*zs)
# print(nums)


nums = [1,2,3,4,3]

nums.remove(3)

print(nums)