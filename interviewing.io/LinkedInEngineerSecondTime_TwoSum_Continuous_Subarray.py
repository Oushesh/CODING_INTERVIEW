#Reference: https://www.youtube.com/watch?v=RxZGHpQhpy4
#Los


'''
1. First question is focussed on Two Sum:
2. Second question is on continuous Subarray, k
'''

'''
The question is only about two Sum:
1. Review of Python in built functions: https://wiki.python.org/moin/TimeComplexity
2.
'''


'''
Pseudocode for Second Question:
Given: list = [1,2,3,4,5,6,7,8,9,10], target = 15, continuous subarray from index 0 to 4, (0,4)

a) Build cummulative list until we reach the target or not exceeding the target
   cum_list = []
   sum = 0
   loop and update sum+=list[i] while sum <= target: index = 0, len(cum_list)

Edge Cases:
1) How long or short can the subarray be? --> If it can also be of one element,
   then just if a in list or if a in set(list) --> O(1) for set worst complexity
   vs O(n) worst complexity for list.

2) We can have negative numbers. Here we assume none.

3) Third edge case, current number during looping > target, skip it
Second example 2:
[4,5,2,3,7,5], target = 12 --> (1,3)


walkthrough interviewer here:
cum_sum = [4,6,9,16] --> stop.
j = 0
sum = 16, target = 12, sum-target = list[j]

return (j+1,i)

sum = 0
cum_sum = set([])
    for i in range(len(list)):
        if list[i]==target:
            return i #index
        else:
            if not list[i] <= target:
                sum+=list[i] #update the the sum
                cum_sum.add(sum) #keeps track of the cummulative sum, we also use set instead of list to optimise on the 'in' operation to optimse from O(n) time complexity to O(1) time complexity
                if not sum <= target:
                    break
                j = 0
                if (cum_sum-target) in list[j]:
                    return (j+1,i)
'''
#This is probably one of the easiest problems of all time
#This one contains the dictionary which reduces the computational complexity from
#O(n²) to O(n)

#This one is proabbly the easiest of all questions
class Numbers:
    def two_sum(self,numbers,target):
        complement = {}
        for number in numbers:
            if number < target:
                complement[number] = target - number
                if complement[number] in numbers:
                    return number, complement[number]

class PatternMatch:
    def search(self,list,target):
        sum = 0
        cum_sum = set([])
        j = 0
        for i in range(len(list)):
            if list[i]==target:
                return i #index where target is found
            elif sum<=target:
                sum+=list[i]
                cum_sum.add(sum)
                if sum==target:
                    #First index, then the current index where we are currently at.
                    return (0,i)
            if sum>target:
                '''
                #here cum_sum > target --> we need to remove the elements from before
                '''
                while sum(list[j:i])> target:
                    #we need a while loop here
                    if (sum-target) in list:
                        #we found our continuous subarray
                        return (j+1,i)
                    else:
                        j+=1

if __name__ == '__main__':
    list = [1,2,3,4,5,6,7,8,9,10]
    #cum_sum = [1,3,6,10,15]
    target = 15
    current_solution = PatternMatch()
    print ('The indices of the subarray is:',current_solution.search(list,target))

    pairs = Numbers()
    numbers  = [3,6,9,12,15,4,2,1,30]
    print ('The 2 numbers whose sum is equal to target are:',pairs.two_sum(numbers,target))
