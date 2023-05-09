# input: nums (arr of ints, sorted in ASCENDING order)
# input: target (int)

# write a func to search target in nums
# if target exists, return index
# otherwise, return -1

# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """

#         left = nums[0]
#         right = nums[len(nums - 1)]
#         center = nums[int(len(nums -1) / 2)]

#         def find_target(nums, target):
#             center = nums[int(len(nums -1) / 2)]
#             center_index = int(len(nums -1) / 2)

#             if len(nums) == 0:
#                 return -1

#             if center > target:
#                 find_target(nums.slice(0,center_index))
#             if center < target:
#                 find_target(nums.slice(center_index, len(nums - 1)))
#             if center == target:
#                 return center_index


# NEETCODE answer


class Solution:
    def search(self, nums, target):

        left, right = 0, len(nums) - 1

        print("l = ", left)
        print("r = ", right)

        while left <= right: # 0 <= 5, 3 <= 5,
            middle = left + ((right - left) // 2)  # (l + r) // 2 can lead to overflow
            print("middle ", middle)   # 4
            print("nums[middle] ", nums[middle]) # 9
            if nums[middle] > target:
                right = middle - 1

            elif nums[middle] < target:
                left = middle + 1

            else:
                return middle
        return -1

nums = [-1,0,3,5,9,12]
#      [ 0,1,2,3,4,5]
target = 9


solution = Solution()
solution.search(nums, target)