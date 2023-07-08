# https://leetcode.com/problems/happy-number/submissions/989630910/
def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    if n == 1:
        return True

    used = [] #keep track of used, otherwise infinite loop
    
    while n != 1:

        s = list(map(int,str(n)))
        tot = 0

        for num in s:
            tot += int(num) ** 2

        if tot == 1:
            return True
        elif tot in used:
            return False
        else:
            used.append(tot)

        n = tot

