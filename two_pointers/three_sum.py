# haha

class Solution:
    def threeSum(self, nums):
        nums.sort()
        l=[]
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                continue

            j=i+1
            k=len(nums)-1
            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if s>0:
                    k-=1
                elif s<0:
                    j+=1
                else:
                    l.append([nums[i],nums[j],nums[k]])
                    j+=1
                    # skip if we found duplicate of j,
                    # dont need to check duplicate of k
                    # because it will automatically skip the duplicate by the adjustment of i and j
                    while nums[j-1]==nums[j] and j<k:
                        j+=1
        return l

# start at i
# j is the next
# k is the end

# [-1,0,1,2,-1,-4]
# [-4, -1, -1, 0, 1, 2]
#   0,  1,  2, 3, 4, 5
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        n = nums.sort()
        ans = []

        for i in range(len(nums)-1):
            # if there are duplicates, continue
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # i = 1,  -1
            # j = 2,  -1
            # k = 5,  2

            j = i + 1
            k = len(nums) - 1

            while(j < k):
                sum = nums[i] + nums[j] + nums[k]
                #  0

                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # j = 3
                    # [-1] == [0]
                    # 3 < 4

                    # i dont understand this part
                    # skip if
                    while nums[j-1]==nums[j] and j<k:
                        j+=1

        return ans