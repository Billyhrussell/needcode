class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
            # .get() is like, if key does not exist, then make one w/ val 0


        for n, c in count.items():
            freq[c].append(n)
            # freq[value].append[key]

        res = []

        # start at end(longest), end at beg
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

