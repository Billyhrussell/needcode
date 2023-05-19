# input: s - string
# (){}[]

# must be open n closed in correct order

# use a stack
# must pop off b4 can move on

def isValid(s):

    matching = {
        ']':'[',
        '}': '{',
        ')': '()'
    }

    stack = []

    for char in s:
        if not stack or char in matching:
            continue
        else:
            stack.append(char)

        stack.pop(-1)

    return not stack