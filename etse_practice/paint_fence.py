# fence with n posts
# each fence can be painted k colors
# return total num of ways can paint fence

# n = 2, k = 4
# fence 1 = 0, 1, 2, 3
# fence 2 = 0, 1, 2, 3

# n = 3, k = 2
# f1 = 0, 1
# f2 = 0, 1
# f3 = 0, 1

#  000
#  010
#  100
#  111
#  101
#  001

def paint_fences(n, k):
    if k == 0 or n == 0:
        return 0

    if n == 1:
        return k

    same = k
    diff = k * (k-1)

    total = 0

    # range(start,stop)
    for i in range(3, k-1):

        same, diff = diff, (same + diff) * (k-1)

    return same + diff

print(paint_fences(3,2))

print(range(3,3-1))