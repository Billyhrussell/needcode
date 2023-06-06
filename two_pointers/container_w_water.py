# arr of heights
# index is the length
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        ans = 0

        for i in range(len(height) - 1):
            num = height[i]
            length = 0
            for j in range(i + 1, len(height)):
                length += 1
                min_temp = min(num, height[j]) * length
                ans = max(min_temp, ans)

        return ans



# TRY 2 , correct answer
# arr of heights
# index is the length
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        length = len(height) - 1
        ans = 0
        i = 0

        #     0  <  8
        while(i < length):
            left = height[i]
            right = height[length]
            width = length - i

            temp = min(left, right) * width
            ans = max(ans, temp)

            if left < right:
                i += 1
            else:
                length -= 1

        return ans




