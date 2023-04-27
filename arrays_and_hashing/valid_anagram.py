# Given two strings s and t, return true if t is an anagram of s,
#  and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of
# a different word or phrase, typically using all the original letters
# exactly once.

# example: s = "anagram", t = "nagaram"
# output: true
# input: s = "rat", t = "car"
# output false

# check if letters in s, match letters in t

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # if lengths are different
        if len(s) != len(t):
            return False

        def letter_counter(letters):
            counter = {}

            for letter in letters:
                if letter in counter:
                    counter[letter] += 1
                else:
                    counter[letter] = 1
            return counter

        s_counter = letter_counter(s)
        t_counter = letter_counter(t)

        for s_letter in s_counter:
            if s_letter not in t_counter or s_counter[s_letter] != t_counter[s_letter]:
                return False

        return True

# NOTES: must account for if not in
# do i need to specify if t_letter not in s_counter? or does this auto check?

s = "anagram"
t = "angaram"

solution = Solution()
print(solution.isAnagram(s,t))

# NEETCODE SOLUTION
class Solution:
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT