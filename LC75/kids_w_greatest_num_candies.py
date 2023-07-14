class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        max_candy = max(candies)

        res = []

        for kid in candies:
            if kid + extraCandies >= max_candy:
                res.append(True)
            else:
                res.append(False)

        return res
