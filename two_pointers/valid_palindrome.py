class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        alpha = 'abcdefghijklmnopqrstuvqxyz'
        strRemoved = ""

        for char in s.lower():
            if char in alpha:
                strRemoved += char

        sL = len(strRemoved) - 1
        half = sL // 2

        for i in range(len(strRemoved) // 2):
            if i <= half:
                if strRemoved[i] != strRemoved[sL]:
                    return False

            sL -= 1

        return True


class Solution(object):
    def isPalindrome(self, s):

        alpha = 'abcdefghijklmnopqrstuvqxyz'
        strRemoved = ""

        for char in s.lower():
            if char in alpha:
                strRemoved += char

        if strRemoved == strRemoved[::-1]:
            return True

        return False