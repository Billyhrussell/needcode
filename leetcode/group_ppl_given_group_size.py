# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/submissions/959257837/

import collections
class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """

        ans = []
        ppl = collections.defaultdict(list)

        for i, group in enumerate(groupSizes):
            ppl[group].append(i)

        for size in ppl:
            groups = ppl[size]
            a = []

            # break into chunks from range (0 - size)
            for i in range(0,len(groups), size):
                x = i
                a = groups[x:x+size]
                ans.append(a)

        return ans
