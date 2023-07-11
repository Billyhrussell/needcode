# class Solution(object):
#     def nthUglyNumber(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """

#         if n == 1:
#             return n

#         ugly = [1]
#         other_primes = []
#         i = 2
#         while len(ugly) < n:
#             if i % 3 == 0 or i % 5 == 0 or i % 2 == 0:
#                 if other_primes:
#                     for num in other_primes:
#                         print("num ", num, " n ", i)
#                         if i % num != 0:
#                             ugly.append(i)
#                 else:
#                     ugly.append(i)
#             else:
#                 other_primes.append(i)
#             i += 1
#         print(other_primes)
#         print(ugly)
#         return ugly[n-1]


# ("ps's: ", 0, 0, 0)
# [1]
# ("t's: ", 2, 3, 5)
# ('temp : ', 2)


# ("ps's: ", 1, 0, 0)
# [1, 2]
# ("t's: ", 4, 3, 5)
# ('temp : ', 3)


# ("ps's: ", 1, 1, 0)
# [1, 2, 3]
# ("t's: ", 4, 6, 5)
# ('temp : ', 4)


# ("ps's: ", 2, 1, 0)
# [1, 2, 3, 4]
# ("t's: ", 6, 6, 5)
# ('temp : ', 5)


# ("ps's: ", 2, 1, 1)
# [1, 2, 3, 4, 5]
# ("t's: ", 6, 6, 10)
# ('temp : ', 6)


# ("ps's: ", 3, 2, 1)
# [1, 2, 3, 4, 5, 6]
# ("t's: ", 8, 9, 10)
# ('temp : ', 8)


# ("ps's: ", 4, 2, 1)
# [1, 2, 3, 4, 5, 6, 8]
# ("t's: ", 10, 9, 10)
# ('temp : ', 9)


# ("ps's: ", 4, 3, 1)
# [1, 2, 3, 4, 5, 6, 8, 9]
# ("t's: ", 10, 12, 10)
# ('temp : ', 10)


# ("ps's: ", 5, 3, 2)
# [1, 2, 3, 4, 5, 6, 8, 9, 10]
# ("t's: ", 12, 12, 15)
# ('temp : ', 12)


# ("ps's: ", 6, 4, 2)
# [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
# ("t's: ", 16, 15, 15)
# ('temp : ', 15)


# ("ps's: ", 6, 5, 3)
# [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15]
# ("t's: ", 16, 18, 20)
# ('temp : ', 16)


def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """

    dp=[1]

    p2,p3,p5=0,0,0

    for i in range(n+1):
        print("ps's: ", p2, p3, p5 )
        t2=dp[p2]*2
        t3=dp[p3]*3
        t5=dp[p5]*5

        print(dp)

        print("t's: ", t2, t3, t5)

        temp=min(t2,t3,t5)

        print("temp : ", temp)

        dp.append(temp)

        if temp==dp[p2]*2:
            print(f"2 temp {temp} dp[p3] {t2}")
            p2+=1


        if temp==dp[p3]*3:
            print(f"3 temp {temp} dp[p3] {t3}")
            p3+=1


        if temp==dp[p5]*5:
            print(f"5 temp {temp} dp[p5] {t5}")
            p5+=1

    return dp[n-1]


print(nthUglyNumber(11))