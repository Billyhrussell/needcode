# input: nums (arr of ints)
# target (int)
# return indices of two nums, such they add to target

# if in map
# target - num = ans
# if ans in nums, return

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        map = {}
        # ans = []

        for i, num in enumerate(nums):
            ans = target - num

            if ans in map:
                return [i, map[ans]]
            else:
                map[num] = i




# given arr if int (nums) & int target
# return index of two nums that add up 2 target

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        map = {}

        for i, num in enumerate(nums):
            ans = target - num
            if ans in map:
                return [i, map[ans]]
            else:
                map[num] = i