class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # cost = [10, 15, 20]
        if not cost:
            return 0

        # dp = [0, 0, 0]
        dp = [0] * len(cost)
        dp[0] = cost[0]
        # dp = [10, 0, 0]

        if len(cost) >= 2:
            dp[1] = cost[1]
        # dp = [10, 15, 0]

        for i in range(2, len(cost)):
            print(i , "i")
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
            # dp[2] = cost[2] + min(dp[2-1], dp[2-2])
            # dp[2] = 20      +     ( 15,  10 )
            # dp[2] = 20 + 10
            # dp[2] = 30

        print(dp)
        return min(dp[-1], dp[-2])


# will either have to start at the first step [cost[0]]
# or start at second step [cost[1]]

# the cost at i is taken from the least pricey previous


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        if not cost:
            return 0

        # dp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        dp = [0] * len(cost)
        dp[0] = cost[0]
        # dp = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]


        if len(cost) >= 2:
            dp[1] = cost[1]
        # dp = [1, 100, 0, 0, 0, 0, 0, 0, 0, 0]

        # dp_in_loop = [1, 100, 2, 3, 3, 103, 4, 5, 104, 0]
        for i in range(2, len(cost)):

            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
            # dp[2] = cost[2] + min(dp[2-1], dp[2-2])
            # dp[2] = 1     +     ( 100,  1 )
            # dp[2] = 1 + 1
            # dp[2] = 2

            # dp[3] = cost[3] + min(dp[3-1], dp[3-2])
            # dp[3] = 1     +     ( 2,  100 )
            # dp[3] = 1 + 2
            # dp[3] = 3

            # dp[4] = cost[4] + min(dp[4-1], dp[4-2])
            # dp[4] = 1     +     ( 3,  2 )
            # dp[4] = 1 + 2
            # dp[4] = 3

            # dp[5] = cost[5] + min(dp[5-1], dp[5-2])
            # dp[5] = 100     +     ( 3,  3 )
            # dp[5] = 100 + 3
            # dp[5] = 103

            # dp[6] = cost[6] + min(dp[6-1], dp[6-2])
            # dp[6] = 1     +     ( 103,  3 )
            # dp[6] = 1 + 3
            # dp[6] = 4

            # dp[7] = cost[7] + min(dp[7-1], dp[7-2])
            # dp[7] = 1     +     ( 4,  103 )
            # dp[7] = 1 + 4
            # dp[7] = 5

            # dp[8] = cost[8] + min(dp[8-1], dp[8-2])
            # dp[8] = 100     +     ( 5,  4 )
            # dp[8] = 100 + 4
            # dp[8] = 104

            # dp[9] = cost[9] + min(dp[9-1], dp[9-2])
            # dp[9] = 1     +     ( 104,  5 )
            # dp[9] = 1 + 5
            # dp[9] = 6

        print(dp)
        return min(dp[-1], dp[-2])
