# can reuse word in dict
# cannot use word if already used by prev s
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        dp = [False] * (len(s) + 1)
        # [False, False, False, False, False, False, False, False, False]
        dp[0] = True
        # [True, False, False, False, False, False, False, False, False]

        n = len(s)
        # 8

        # 1, 2, 3, 4, 5, 6, 7, 8
        for i in range(1, n+1):
            print(dp)
            # 0 1
            for j in range(i):
                # dp[0] = True and s[1,0]
                print("i: ", i, " j: ", j)
                print("dp[j] ", dp[j], " s[j:i] ", s[j:i])
                if dp[j] and s[j:i] in wordDict:
                    print("in if")
                    dp[i] = True
                    break
        print(dp)
        return dp[n]


# CATSANDOG
# [True, False, False, False, False, False, False, False, False, False]


#  i = 1, 2, 3, 4, 5, 6, 7, 8, 9

# i = 1
# j : 0
# s[j:i] = C

# i = 2
# j : 0, 1
# s[j:i] = CA, C

# i = 3
# j : 0, 1, 2
# s[j:i] = CAT, AT, T
# [True, False, False, True, False, False, False, False, False, False]

# i = 4
# j : 0, 1, 2, 3
# s[j:i] = CATS, ATS, TS, T
# [True, False, False, True, False, False, False, False, False, False]


# i = 5
# j : 0, 1, 2, 3, 4
# s[j:i] = CATSA, ATSA, TSA, TA, A

# i = 6
# j : 0, 1, 2, 3, 4, 5
# s[j:i] = CATSAN, ATSAN, TSAN, TAN, AN, N

# i = 7
# j : 0, 1, 2, 3, 4, 5, 6
# s[j:i] = CATSAND, ATSAND, TSAND, TAND, AND, ND, D

# i = 8
# j : 0, 1, 2, 3, 4, 5, 6, 7
# s[j:i] = CATSANDO, ATSANDO, TSANDO, TANDO, ANDO, NDO, DO, O


# i = 9
# j : 0 , 1, 2, 3, 4, 5, 6, 7, 8
# s[j:i] = CATSANDOG, ATSANDOG, TSANDOG, TANDOG, ANDOG, NDOG, DOG, OG, G


