# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        num_letters = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        ans = []

        for key in num_letters:
            num_letters[key] = list(num_letters[key])

        if len(digits) == 1:
            return num_letters[digits]

        # digit_list = list(map(int, digits))
        digit_list = list(digits)

        for i, num in enumerate(digit_list):
            # if len(digits) > 3, set temp = ans after 2
            if i == len(digit_list) - 1:
                break
            temp = num_letters[num]
            print(num, "char at")
            for char in num_letters[digit_list[i+1]]:
                for j in range(len(temp)):
                    ans.append(temp[j] + char)

            print(i, len(digit_list))

        return ans