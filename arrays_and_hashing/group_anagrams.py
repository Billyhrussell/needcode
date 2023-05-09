# # input: arry of strings (strs)
# # group anagrams together
# # return arr[arrs] of anagrams grouped

# # anagram is same word written differently

# class Solution(object):
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """

#         countList = []
#         anagrams = []

#         def countStr(str):
#             counter = {}

#             for char in str:
#                 if char in counter:
#                     counter[char] += 1
#                 else:
#                     counter[char] = 1

#             return counter

#         for str in strs:
#             countList.append(countStr(str))

#         # print(countList)

#         def counter(countList, strs):
#             first_count = countList[0]
#             matching_anagrams = []
#             remaining = []
#             matching_anagrams.append(strs[0])

#             # print("strs = ", strs)
#             # print("countList = ",countList)

#             for i, count in enumerate(countList[1:]):
#                 if count == first_count:
#                     print("COUNT = ", count)
#                     print("First_COUNT = ", first_count)
#                     print(i)
#                     matching_anagrams.append(strs[i+1])
#                 else:
#                     remaining.append(strs[i+1])

#             # return matching_anagrams
#             return [matching_anagrams, remaining]

#         print("CPINTER", counter(countList,strs))


#         initial_grab = counter(countList, strs)
#         anagrams.append(initial_grab[0])

#         while len(initial_grab[1]) > 1:
#             grab2 = counter(countList, initial_grab[1])
#             anagrams.append(grab2[0])
#             initial_grab = grab2[1]

#         return anagrams

# strs = ["eat","tea","tan","ate","nat","bat"]
# solution = Solution()
# print(solution.groupAnagrams(strs))

# from collections import defaultdict
import collections

#create an empty dictionary (ans)
# iterate over single str in strs
# create an empty array with 26 indexs
# for every char in str
# set the count to the chars in the str
# set the ans/dictionary with the key of chars : appending the value of string
# return the ans.values() (returns a list of list)
#

class Solution:
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1    #ord returns integer representing unicode character (A = 65)

            ans[tuple(count)].append(s)

        return ans.values()

# print(ord('t'))
# print(ord('a'))

# count = [0] * 26 =
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# count =
# [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
# [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
# [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
# [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
# tuple(count) =
# (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
# (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
# (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
# (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
# (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
# (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
# ans =
# {(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
# : ['eat', 'tea', 'ate'],
# (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0):
# ['tan', 'nat'],
# (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0):
# ['bat']})
# ans.values() =
#  [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

strs = ["eat","tea","tan","ate","nat","bat"]
solution = Solution()
print(solution.groupAnagrams(strs))

import collections

class Solution(object):
    def groupAnagramsExplained(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        ans = collections.defaultdict(list)
        # CREATE empty dict (key:value)

        for str in strs:
            character_list = [0] * 26
            # CREATE list of length:26, each initialized to 0
            # letter a @ index 0, letter z @ index 25

            for char in str:
                character_list[ord(char) - ord('a')] += 1
                # SET the index of the letter in character_list

            ans[tuple(character_list)].append(str)
            # SET the key to the array of letters
            # SET the value to the string that matches the array

        return ans.values()
        # RETURN a list of values


import collections

# create hashmap (empty)
# key: 26 arrs of 0, changed to the amt of letters
# value: the strs that match the key
# return hashmap.values()

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        ans = collections.defaultdict(list)
        # initialize empty dict (no key errors)

        for str in strs:
            setList = [0] * 26
            # setting list to 26 0's

            for char in str:
                setList[ord(char) - ord('a')] += 1

            ans[tuple(setList)].append(str)

        return ans.values()


# create hashmap (key val pairs)
# where key = arr of 26
# where val = matching str to key

def group_anagrams(strs):
    ans = collections.defaultdict(list)

    for str in strs:
        lettersList = [0] * 26

        for char in str:
            lettersList[ord(char) - ord('a')] += 1

        ans[tuple(lettersList)].append(str)

    return ans.values()

