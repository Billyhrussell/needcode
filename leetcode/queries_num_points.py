# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/solutions/3284192/easy-python-solution-run-time-88-9/
class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        lst=[]
        for i in queries:
            count=0
            x1=i[0]
            y1=i[1]
            r=i[2]
            for j in points:
                if sqrt((x1-j[0])**2 + (y1-j[1])**2)<=r:
                    count+=1
            lst.append(count)
        return lst