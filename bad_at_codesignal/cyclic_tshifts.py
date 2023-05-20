# idk i failed this
# cyclic tshifts ?
# given two arrays of same len
# t = len(a1) - 1
# cycle the first arr t amount of times
# return arr w/ the sum of a[0] - b[0]
# b arr stays the same

# EX :
# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# (1-5), (2-6), (3-7), (4-8)
# if negative, revert to pos
# (4 + 4 + 4 + 4)
# [16, ]

# a(cycle0) = [1, 2, 3, 4]
# a(cycle1) = [4, 1, 2, 3]
# a(cycle2) = [3, 4, 1, 2]
# a(cycle3) = [2, 3, 4, 1]

def find_cycle_diff_sum(nums1, nums2):

    arr_of_arrs = []
    arr_of_arrs.append(nums1)
    ans = []

    def cycle(n1):
        new_arr = []
        temp = n1.copy()

        new_arr.append(temp.pop())

        for num in temp:
            new_arr.append(num)

        return new_arr

    # print("cycled ", cycle(nums1))
    for i in range(len(nums1))[1::]:
        arr_of_arrs.append(cycle(arr_of_arrs[i-1]))

    for arr in arr_of_arrs:
        diff = 0
        for i, num in enumerate(arr):
            temp = num - nums2[i]
            if temp < 0:
                temp *= -1
            diff += temp
        ans.append(diff)

    return ans

nums1 = [7, 11, 12, 8]
nums2 = [2, 5, 1, 9]
print(find_cycle_diff_sum(nums1, nums2))

