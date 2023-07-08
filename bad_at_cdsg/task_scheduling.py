# two servers, paid and free.
# free can only be used if paid is occupied

# ith task takes time[i] to complete
# ith task is cost[i]

# free server cost is 0, time is 1

# def task_scheduling(n, cost, time):

#     ans = 0

#     for i in range(n):
#         print(i)
#         ans += cost[i]
#         i = 30

#     return ans

# # n = 4

# # cost = [1,2,3,2]
# # time = [1,2,3,2]
# #
# # print(task_scheduling(n, cost, time))

# c=[1,1,3,4]
# t=[3,1,2,3]
# n=len(c)

# from functools import cache

# @cache
# def f(i,j):  # for the ith task choose either paid or free
#     if i==n:
#         return [float('inf'),0][j>=0]

#     return min(c[i]+f(i+1,j+t[i]), f(i+1,j-1))

# return f(0,0)

# def task_scheduling1(n, cost, time):

#     @cache
#     def f(i,j):  # for the ith task choose either paid or free
#         if i==n:
#             return [float('inf'),0][j>=0]

#         return min(c[i]+f(i+1,j+t[i]), f(i+1,j-1))

#     return f(0,0)

# cost =[1,8,8,16,16]
# time=[1,2,1,4,10]
# n = len(cost)
# # cost = [1,1,3,4]
# # time = [3,1,2,3]
# # print(task_scheduling1(n, cost, time))

# c = [1,2,3,2]
# t = [1,2,3,2]
# n = len(c)

# def f(i, j, memo):
#     if i == n:
#         return [float('inf'), 0][j >= 0]
#     if (i, j) in memo:
#         return memo[(i, j)]

#     result = min(c[i] + f(i + 1, j + t[i], memo), f(i + 1, j - 1, memo))
#     memo[(i, j)] = result

#     return result

# memo = {}
# print(f(0, 0, memo))

# def getMinCost(cost, time):
#     total_cost = 0
#     max_time = 0

#     for t in time:
#         max_time = max(max_time, t)

#     for i in range(len(cost)):
#         if time[i] == max_time:
#             total_cost += cost[i]
#         else:
#             total_cost += min(cost[i], 0)

#     return total_cost

cost = [1, 1, 3, 4]
time = [3, 1, 2, 3]


# print(getMinCost(cost, time))

# def getMinCost(cost, time):
#     total_cost = 0
#     free_server_busy = False
#     max_time = 0

#     for t in time:
#         max_time = max(max_time, t)

#     for i in range(len(cost)):
#         if time[i] == max_time:
#             if free_server_busy:
#                 total_cost += cost[i]
#             else:
#                 free_server_busy = True
#         else:
#             total_cost += min(cost[i], 0)

#     return total_cost

# cost = [1, 1, 3, 4]
# time = [3, 1, 2, 3]

# print(getMinCost(cost, time))

def getMinCost(cost, time):
    total_cost = 0
    is_paid_server_busy = False

    for i in range(len(cost)):
        if not is_paid_server_busy:
            total_cost += cost[i]
            is_paid_server_busy = True
        else:
            if cost[i] <= 0:  # Running the task on the free server is cheaper or equal cost
                total_cost += cost[i]
            else:  # Running the task on the paid server is cheaper
                total_cost += cost[i]
                is_paid_server_busy = False

    return total_cost


cost = [1, 1, 3, 4]
time = [3, 1, 2, 3]

print(getMinCost(cost, time))

