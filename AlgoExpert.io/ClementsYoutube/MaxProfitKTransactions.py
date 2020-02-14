#Max Profit
#Profit = Selling - Buying
#Sell after buy

#Dynamic Programming

#Sample input: [5,11,3,50,90], 2
#Sample output: 93 (Buy:5, Sell:11;Buy:3,Sell:90)

# O(nk) Time Complexity | O(nk) Space Complexity
def maxProfitwithKTransactions(prices, k):
    #edge case.
    if not len(prices):
        return 0

    #Build a 2D Profit Matrix:
    profits = [[0 for d in prices] for t in range(k+1)]

    #Assign the max_Profit to -inf.
    for t in range(1,k+1):
        max_until_now = float("-inf")
        for d in range(1,len(prices)):
            max_until_now = max(max_until_now, profits[t-1][d-1]-prices[d-1])
            profits[t][d] = max(profits[t][d-1],max_until_now+prices[d])
    return profits[-1][-1]

#Can we do be better for the space complexity?
#Well, previously we were saving the whole array.
#But instead we could only save the previous row.

def second_version(prices,k):
    #edge case.
    if not len(prices):
        return 0

    #Define previous & current row profits
    oddProfits = [0 for d in prices]
    evenProfits = [0 for d in prices]

    for t in range(1,k+1):
        max_until_now = float("-inf")
        if t%2==1:
            currentProfits = oddProfits
            previousProfits = evenProfits
        else:
            currentProfits = evenProfits
            previousProfits = oddProfits

        for d in range(1,len(prices)):
            max_until_now = max(max_until_now,previousProfits[d-1]-prices[d-1])
            currentProfits[d] = max(currentProfits[d-1],max_until_now+prices[d])
    return evenProfits[-1] if k%2 == 0 else oddProfits[-1]

#Test the Function below:
if __name__ == '__main__':
    prices = [5,11,3,50,60,90]
    k      = 2
    output = maxProfitwithKTransactions(prices,k)
    second_output = second_version(prices,k)
    print (output)
    print (second_output)
