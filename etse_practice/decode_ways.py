# def numDecodings( s):
#     """
#     :type s: str
#     :rtype: int
#     """

#     total = 0
#     nums = [int(i) for i in s]


#     # nums = [int(i) for i in nums]

#     for i in range(len(nums))[:len(nums)-1]:
#         if nums[i] == 0:
#             breakpoint()
#             continue
#         elif chr(nums[i]) and nums[i+1] != 0:
#             temp = str(nums[i]) + str(nums[i+1])
#             print(temp)
#             if chr(int(temp)):
#                     total += 1
#             total += 1
#         elif chr(nums[i]) and nums[i+1] == 0:
#             breakpoint()

#             total += 1

#     return total

# print(numDecodings("226"))



def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """

    # ord, char


    dp = [0] * (len(s) + 1 )
    print(dp)

    # dp[0] is always the base case, always want it to be true
    # should always len()+1, b/c
    dp[0] = 1
    dp[1] = 0 if s[0] == "0" else 1

    for i in range(2, len(s) + 1):

        # s[i-1:i] -> this ENDS before i
        # s[2-1:2]
        # s[1:2] -> 2

        # s[3-1:3]
        # s[2:3] -> 6
        if 0 < int(s[i-1:i]) <= 9:
            dp[i] += dp[i-1]

        # s[2-2:2]
        # s[0:2] -> 22

        # s[3-2:3]
        # s[1:3] -> 26
        if 10 < int(s[i-2:i]) <= 26:
            dp[i] += dp[i-2]

    print(dp)

    return dp[len(s)]


print(numDecodings("226"))