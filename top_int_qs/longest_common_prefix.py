# ONLY WORKS IF PREFIX IS IN THE FIRST STRING....

# ["flower","flow","flight"]

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # f
        pre = strs[0]

        # flower
        for i in strs:
            # 
            while not i.startswith(pre):
                pre = pre[:-1]

        return pre