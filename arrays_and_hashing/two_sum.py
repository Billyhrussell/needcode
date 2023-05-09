# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# You can return the answer in any order.

# given [3,2,4], target = 6
# output: [1,2]

# given array of ints and target num
# return index of 2 nums that add up to target

# want to add 2 nums together
# [1,2,4,5,10,12]
# select first and check if matches with every num behind
# if not, pop num off and check w/remaining nums

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        ans = []

        def get_nums(nums,target):

            first_num = nums[0]
            nums_cont = nums[1:]
            values = []

            print("first_num ", first_num, "nums_cont ", nums_cont)

            for num in nums_cont:
                print(first_num, "first_num", num, "num in nums_cont")
                if first_num + num == target:
                    print("in if")

                    values = [first_num, num]
                    # print(values, "vals in if")
                else:
                    get_nums(nums_cont, target)

            # print(values, "values")
            return [1,1]

        values = get_nums(nums, target)

        print(values)

        # for index, num in enumerate(nums):
        #     if num == values[0] or values[1]:
        #         ans.append(index)


        return ans

solution = Solution()
print(solution.twoSum([3,2,4], 6))

# solution = Solution()
# print(solution.isAnagram(s,t))


# want to add 2 nums together
# [1,2,4,5,10,12]
# select first and check if matches with every num behind
# if not, pop num off and check w/remaining nums
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        first_num = nums[0]
        ans = []

        def find_ans(nums, target):
            for num in nums[1:]:
                if num + first_num == target:
                    ans = [num, first_num]
                    return ans

            return False

# SECOND_ATTEMPT

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums_copy = list(nums)
        nums_sum = []
        ans = []

        while len(nums_sum) != 2:
            first_num = nums_copy[0]
            nums_copy.pop(0)

            for num in nums_copy:
                if num + first_num == target:
                    nums_sum.append(num)
                    nums_sum.append(first_num)

        for i, n in enumerate(nums):
            if n == nums_sum[0] or n == nums_sum[1]:
                ans.append(i)
        return ans

nums = [3,2,4]
target = 6

solution = Solution()
print(solution.twoSum(nums,target))

# NEETCODE ANSWER
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        # for index, num in nums
        for i, n in enumerate(nums):
            diff = target - n           #difference = target - num
            if diff in prevMap:         #if the difference is in the map,
                return [prevMap[diff], i] #return the index
            prevMap[n] = i                 #or add it to the map


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        prevMap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[num] = i








# input: arr of int, nums
# int, target
# return indices of two nums, such that they add up to target
# [2,7,11,15]

def twoSum(nums, target):

    map = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in map:
            return [map[diff], i]
        map[num] = i

# TWO-SUM
# create a map to store key of num, value of index
# enumerate over
# set a difference
# if diff in map, return map key and curr index
# set index 