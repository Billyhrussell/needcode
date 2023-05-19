# input: nums (int arr)
# return: t if appears at least 2x
# f if every elem appears 1x

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        counter = {}

        for num in nums:
            if num in counter:
                return True
            else:
                counter[num] = 1

        return False