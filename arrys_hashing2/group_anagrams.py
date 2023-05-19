# input: strs (arr of strs)
# group anagrams together
# return grouped anagrams

import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        ans = collections.defaultdict(list)

        for str in strs:
            alpha = [0] * 26

            for char in str:
                alpha[ord(char) - ord('a')] += 1

            ans[tuple(alpha)].append(str)

        return ans.values()