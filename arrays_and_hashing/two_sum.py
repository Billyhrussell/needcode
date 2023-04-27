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

