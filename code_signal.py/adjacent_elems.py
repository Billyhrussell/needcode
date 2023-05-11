# Given an array of integers
# find the pair of adjacent elements that has the largest product
# return that product.

# ex: inputArray = [3, 6, -2, -5, 7, 3]
# output: solution(inputArray) = 21

def solution(inputArray):

    stack = []
    ans = []

    if len(inputArray) == 2:
        return inputArray[0] * inputArray[1]

    for num in inputArray:
        if not stack:
            stack.append(num)
            continue

        ans.append(num * stack[-1])
        stack.pop(-1)
        stack.append(num)

    return max(ans)


print(solution([5, 1, 2, 3, 1, 4]))