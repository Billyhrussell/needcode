# arr = 2, 5, -3
# O(n^2)
def perfectPairs(arr):
    ans = 0

    for i, num in enumerate(arr):
        x = num
        for n in arr[i+1::]:
            y = n

            minus = abs(x - y)
            plus = abs(x + y)

            x = abs(x)
            y = abs(y)

            if min(minus, plus) > min(x,y):
                continue
            elif max(minus,plus) < max(x,y):
                continue

            ans += 1


    return ans

# arr = [2,5,-3]
arr = [-9, 6, -2, 1]

print(perfectPairs(arr))

# O(n)
def perfect_pairs(arr):
    n = len(arr)
    arr.sort()
    left, right = 0, n - 1
    count = 0
    while left < right:
        x, y = arr[left], arr[right]
        if min(abs(x-y), abs(x + y)) <= min(abs(x), abs(y)) and max(abs(x-y), abs(x + y)) >= max(abs(x), abs(y)):
            count += (right - left)
            left += 1
        else:
            right -= 1
    return count

# 0(n^2)
def perfect_pairs(arr):
    n = len(arr)
    arr.sort()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            x, y = arr[i], arr[j]
        if min(abs(x-y), abs(x + y)) > min(abs(x), abs(y)):
            break
        if max(abs(x-y), abs(x + y)) < max(abs(x), abs(y)):
            continue
        count += 1
    return count