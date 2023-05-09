# Given a string
# s = '(', ')', '{', '}', '[', ']'
#  determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Input: s = "()[]{}"
# Output: true

# Last in first out
# always removing at top of list/stack - a hint to use a stack


class Solution(object):
    def isValid(self, str):
        """
        :type s: str
        :rtype: bool
        """

        correct_order = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        stack = []          # [( ]


        # )
        for char in str:
            if char not in correct_order:
                stack.append(char)
                continue
            # if stack is empty or the end of stack != end char
            if not stack or stack[-1] != correct_order[char]:
                # stack[-1] = (
                # correct_order[')'] = (
                # if ( != (
                return False
            stack.pop()

        return not stack

class Solution(object):
    def isValid(self, str):
        """
        :type s: str
        :rtype: bool
        """

        Map = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        stack = []

        for char in str:
            if char not in Map:
                stack.append(char)
                continue
            if not stack or stack[-1] != Map[char]:
                return False
            stack.pop()

        return not stack

# given string w  {}, [], ()
# determine if input string is valid
# valid if open brackets closed by same type of bracket
# must be closed in correct order
# every close bracket has open bracket of same type

class Solution(object):
    def isValid(self, str):
        """
        :type s: str
        :rtype: bool
        """

        valid = {'}' : '{',
                ']' : '[',
                ')' : '('}

        stack = []

        for s in str:
            if s not in valid:
                stack.append(s)
                continue
            if not stack or stack[-1] != valid[s]:
                return False
            stack.pop()

        return not stack


# iterate over string
# if char not in valid_choice
# add to stack
# if not stack (if stack is empty)
#           or if end of stack does not = valid_choice[char]
# return false

# WITH STACKS YOU MUST CHECK AT THE END