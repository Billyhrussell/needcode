# input: nums, an integer array
# input: k, an integer

# return: the k most frequent elements

# nums = [1,1,1,2,2,3], k = 2

# my_solution
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """

    counter = {}
    ans = []

    for num in nums:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1

    for num in counter:
        if counter[num] >= k:
            ans.append(k)

    return ans


# neetcode_solution with my notes

class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        # freq = [[], [], [], [], [], [], []]

        for n in nums:
            count[n] = 1 + count.get(n, 0) #if key does not exist, set value to 0


        # count = {1: 3, 2: 2, 3: 1}
        for n, c in count.items():
            # count.items() = [(1, 3), (2, 2), (3, 1)]
            # .items() is tuple for each key/val pair
            # (n, c), (n, c), (n, c)

            freq[c].append(n)

        # freq = [[], [3], [2], [1], [], [], []]

        res = []
        for i in range(len(freq) - 1, 0, -1):
        # for i in range(start, stop, step)
        # range(6, 0, -1)
        # range is stepping BACK
        # 6, 5, 4, 3, 2, 1

            for n in freq[i]:

                # for a num inside of frequency arr
                res.append(n)
                # append num
                if len(res) == k:
                    print("res ", res)
                    # if the length of the res == k
                    return res

nums = [1,1,1,2,2,3]
k = 2
solution = Solution()
print(solution.topKFrequent(nums, k))

# MUST RETURN ELEMENTS WITH THE HIGHEST FREQUENCY
# not OF the highest frequency

# From leetcode comments:
# The point of the problem is not to return elements that have frequency of K or more, but to return K most frequent elements.
# So, assume you have the following input:
# nums = [ 1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 5 ],
# k = 2

# if you create a frequency table:
# i | f
# ---
# 1 | 3
# 2 | 2
# 3 | 1
# 4 | 3
# 5 | 2

# then you have to return the 2 elements with the highest frequency from it (in this case i=1 and i=4)

# input: int arr, nums
#  int k,
# return the k most frequent elements


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res