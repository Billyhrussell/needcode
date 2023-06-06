# https://leetcode.com/problems/permutation-in-string/
# class Solution(object):
#     def checkInclusion(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: bool
#         """
#         # temp = ""


#         def letterCounter(s):
#             map = {}
#             for char in s:
#                 if char in map:
#                     map[char] += 1
#                 else:
#                     map[char] = 1
#             return map


#         for i in range(len(s2)):
#             temp = ""
#             j = 0
#             while(len(temp) < len(s1) and i < len(s2)-(len(s1)-1)):
#                 temp += s2[i + j]
#                 print("i ", i, " temp ", temp, " j ", j)
#                 j += 1


#             t1 = letterCounter(s1)
#             t2 = letterCounter(temp)

#             if t1 == t2:
#                 return True

#         return False

# TODO: WORKS BUT SUCKS:

# class Solution(object):
#     def checkInclusion(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: bool
#         """
#         # temp = ""


#         def letterCounter(s):
#             map = {}
#             for char in s:
#                 if char in map:
#                     map[char] += 1
#                 else:
#                     map[char] = 1
#             return map

#         t1 = letterCounter(s1)

#         for i in range(len(s2)):
#             temp = ""
#             j = 0
#             # while(len(temp) < len(s1) and i < len(s2)-(len(s1)-1)):
#             #     temp += s2[i + j]
#             #     print("i ", i, " temp ", temp, " j ", j)
#             #     j += 1
#             temp = s2[i:i+len(s1)]

#             t2 = letterCounter(temp)

#             if t1 == t2:
#                 return True

#         return False

#         temp = s2[i::3]

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        def letterCounter(s):
            map = {}
            for char in s:
                if char in map:
                    map[char] += 1
                else:
                    map[char] = 1
            return map

        t1 = letterCounter(s1)

        for i in range(len(s2)):
            temp = s2[i:i+len(s1)]

            t2 = letterCounter(temp)

            if t1 == t2:
                return True

        return False