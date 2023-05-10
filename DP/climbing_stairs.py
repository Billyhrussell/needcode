# you are climbing a staircase
# n steps to top
# can climb 1 or 2 steps
# how many was can you climb to the top?

#         5
# 1 1 1 1 1
# 1 1 1 2
# 2 1 1 1
# 1 2 1 1
# 1 1 2 1
# 1 2 2
# 2 2 1
# 1 2 1

# distinct(n) = distinct(n-1) + distinct(n-2)

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2

        # creates array of 0's
        dp = [0] * (n+1)

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            # range is [1, 2, 3]
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]


# n = 4
# 1 1 1 1
# 2 1 1
# 1 2 1
# 1 1 2
# 2 2
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo ={}
        memo[1] = 1
        memo[2] = 2

        # memo = {1: 1,
        #         2: 2,
        #         4: }
        def climb(n):
            if n in memo: # if the recurssion already done before first take a look-up in the look-up table
                return memo[n]
            else:   # Store the recurssion function in the look-up table and reuturn the stored look-up table function
                memo[n] =  climb(n-1) + climb(n-2)
                            # climb(4-1) + climb(4-2)
                            # 3 +  2 = 5
                            # climb(3-1) + climb(3-2)
                            # = 2 + 1 = 3


                return memo[n]

        return climb(n)


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        steps = {}
        steps[1] = 1
        steps[2] = 2

        def climb(n):
          if n in steps:
            return steps[n]
          else:
            steps[n] = climb(n-1) + climb(n-2)
            return steps[n]

        return climb(n)
        