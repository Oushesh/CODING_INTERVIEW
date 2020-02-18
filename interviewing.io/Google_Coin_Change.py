'''
Coin Change Python interview: Google
Reference: https://www.youtube.com/watch?v=HWW-jA6YjHk&feature=emb_rel_end
'''

'''
33 cents: 1 quarter(25), 1. nickel(5), 1 pennies(1)
Define: list_coins available:
coins = [25,10,5,1]
Itereativiely divide until no remainder.
Lets try Greedy approach first.
'''

'''
Search Algorithm: BFS
'''

'''
Dynamic Programming. Induction
[25,10,5,1]
if I need it, I use 0 or 1
O coins chosen: [0,0,0,0]
[1,0,1,1] #right  choice.

Condition of check: total - value of coin = remainder.
how to decide if to take or not? well check if total exceeds.
check if the the remainder is inside the array.

'''
class Solution():
    def min_coins_greedy(self,cents,coins):
        if cents < 1:
            return 0
        num_coins = 0
        for coin in coins:
            num_coins += int(cents/coin)
            cents = cents % coin
            if cents == 0:
                break
        return num_coins
    '''
    Dynamic Programming approach
    Assuming all coins used max once. First case
    '''
    def min_coins_dp(self,cents,coins):
        choice = [0 for coin in coins] #initialize the starting list
        sum = 0
        for i in range(len(coins)):
            if (sum+coins[i]) <= cents:
                choice[i] = 1 #set to one: i chose
                #at each coin I have a choice:
                sum +=coins[i]
        return choice
    '''
    now what if we could use coins more than once?
    let's modify the first code: add a remainder check:
    cents  = 72, expected answer: [2,2,0,1]
    TOCHECK: Nice
    '''
    def min_coins_multi_dp(self,cents,coins):
        if cents <1:
            return 0
        sum = 0
        num_coins = 0
        remainder = 0
        choice = [0 for i in coins]
        for i  in range(len(coins)):
            if (sum+num_coins*coins[i])<=cents:
                num_coins=int(cents/coins[i])
                remainder = cents%coins[i]
                choice[i]=num_coins #changed to the answer of the divisor
                sum +=num_coins*coins[i]
        return choice

if __name__ == "__main__":
    coins = [25,10,5,1]
    cents = 72
    output = Solution()
    print ('The number of coins',output.min_coins_greedy(cents,coins))

    print ('The number of coins',output.min_coins_dp(cents,coins))

    print ('The number of coins multiple:',output.min_coins_multi_dp(cents,coins))
