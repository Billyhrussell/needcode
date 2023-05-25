class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        ans = []
        map = {}

        for i, num in enumerate(numbers):
            temp = target - num
            if temp in map:
                return [map[temp] + 1, i + 1]
            else:
                map[num] = i