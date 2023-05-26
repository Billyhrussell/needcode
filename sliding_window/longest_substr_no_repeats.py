# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """

#         longest = ""
#         ans = []

#         for char in s:
#             if char in longest:
#                 ans.append(longest)
#                 longest = char

#             else:
#                 longest += char

#         print(ans)
#         tot = len(ans[0])

#         for i in range(len(ans) - 1):
#             next = ans[i + 1]

#             if tot < len(next):
#                 tot = len(next)

#         return tot

# try 2 407 testcases passed
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """

#         if len(s) == 0:
#             return 0
#         if len(s) == 1:
#             return 1

#         substr = ""
#         lengths = []

#         for i, char in enumerate(s):
#             if char in substr:
#                 lengths.append(len(substr))
#                 substr = char
#             else:
#                 substr += char
#                 if i == len(s)-1:
#                     lengths.append(len(substr))

#         return max(lengths)


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        substr = ""
        lengths = []
        strs = []

        for i, char in enumerate(s):
            if char in substr:
                strs.append(substr)
                lengths.append(len(substr))
                if s[i] == s[i-1]:
                    substr = char
                else:
                    temp = substr.split(char)
                    substr = temp[-1] + char

            else:
                substr += char
                if i == len(s)-1:
                    lengths.append(len(substr))
                    strs.append(substr)

        return max(lengths)
