def getMinimumOperations(executionTime, x, y):

    ans = 0

    while(len(executionTime) > 0):
        majorJob = max(executionTime)

        t1 = []

        k = executionTime.index(majorJob)
        for i, num in enumerate(executionTime):
            if i == k:
                temp = num - x
                if temp > 0:
                    t1.append(temp)
            else:
                temp = num - y
                if temp > 0:
                    t1.append(temp)

            executionTime = t1

        ans += 1

    return ans


# executionTime = [3,4,1,7,6]
# x = 4
# y = 2

executionTime = [2,3,5]
x = 3
y = 1
print(getMinimumOperations(executionTime, x, y))