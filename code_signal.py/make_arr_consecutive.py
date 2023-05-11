
# input: int arr status of diff sizes
# non-negative

# arrange from smallest to largest
# prev must inc exactly by 1
# how many additional needed for inc by 1?

# ex: statues = [6, 2, 3, 8]
#  [2, 3, -, -, 6, -, 8]
# need 3 to make complete

def solution(statues):
    min_val = min(statues)
    max_val = max(statues)

    needed = 0

    for num in range(min_val, max_val):
        if num not in statues:
            needed += 1

    return needed

print(solution([6,2,3,8]))