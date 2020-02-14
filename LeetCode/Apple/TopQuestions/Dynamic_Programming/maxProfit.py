#Selling needs to be after buing
#and bigger
class Solution:
    def maxProfit(self,prices):
        #edge case.
        if len(prices)<2:
            return 0
        max_profit = float('-inf')
        buy = prices[0]
        for d in range(1,len(prices)):
            if prices[d]<buy:
                buy=prices[d]
            profit = prices[d]-buy
            if profit > max_profit:
                max_profit=profit
        return max_profit

if __name__ == "__main__":
    prices = [7,15,3,6,4]
    #Brute force would be compute all the profits:
    #
    output = Solution()
    print ('The maximum Profit is :',output.maxProfit(prices))
