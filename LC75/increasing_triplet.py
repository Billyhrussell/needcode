# def increasingTriplet(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """

#         for i in range(1, len(nums) -1):
#             if nums[i-1] < nums[i] and nums[i] < nums[i+1]:
#                 return True

#         return False

# def increasingTriplet(self, nums):
#     """
#     :type nums: List[int]
#     :rtype: bool
#     """

#     ctr = {}
#     for i in range(len(nums)):
#         ctr[nums[i]] = i

#     s = sorted(ctr.keys())

#     # for i in range(1, len(s)):
#     #     if ctr[i-1] < s[i] and s[i] < s[i+1]:


#     for i, key in enumerate(s, 1):
#         if s[i-1] < s[i] and s[i] < s[i+1]:
#             if ctr[s[i-1]] < ctr[s[i]] and ctr[s[i]] < ctr[s[i+1]]:
#                 return True

#     return False

def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    # ctr = {}
    # for i in range(len(nums)):
    #     ctr[nums[i]] = i

    # s = sorted(ctr.keys())

    # # for i in range(1, len(s)):
    # #     if ctr[i-1] < s[i] and s[i] < s[i+1]:

    # for i in range(1, len(s)-1):
    #     if s[i-1] < s[i] and s[i] < s[i+1]:
    #         if ctr[s[i-1]] < ctr[s[i]] and ctr[s[i]] < ctr[s[i+1]]:
    #             return True

    # return False

    first = second = float('inf')
    for n in nums:
        print(n,  first , second)
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False

print(increasingTriplet([1,2,3,4,5]))