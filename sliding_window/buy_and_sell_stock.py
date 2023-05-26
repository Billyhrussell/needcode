# attempt 1, fails @ test_case 198
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        maxProfit = 0

        for i in range(len(prices)):
            buy_day = prices[i]
            temp = i + 1
            while( temp < len(prices)):
                sell_day = prices[temp]
                profit =  sell_day - buy_day
                maxProfit = max(maxProfit, profit)
                temp += 1


        return maxProfit

class Solution:
    def maxProfit(self,prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit