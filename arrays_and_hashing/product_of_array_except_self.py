# input: int array nums
# return: array ans, such that ans[i] = product of all elems nums, except nums[i]

# [1,2,3,4]
# [24,12,8,6]

# create hashmap w/ key-val pairs
# 1: 2*3*4
# 2: 1*3*4

import numpy
import copy

# my ans
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        ans = {}


        for i in range(len(nums)):
            nums_copy = copy.copy(nums)
            nums_copy.pop(i)

            ans[i] = numpy.prod(nums_copy)

        return ans.values()



nums = [1,2,3,4]
solution = Solution()
print(solution.productExceptSelf(nums))
# [24,12,8,6]


# needcode_answer


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res