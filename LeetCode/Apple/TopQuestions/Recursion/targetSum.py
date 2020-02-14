'''
Example:
input:[8,1,2,3,-5,4,5,6]
target:
#Lets use the holy grail of Dynamic Programming
'''

'''
Describe me your thought patterns:
#in 1 loop time. O(n) or O(nlogn)
#check digitwise if num[i]==target:
#set starting index,i to num[0]; iteratively update the sum as long as
#the sum is less than the target.
#how to decide whether I want to add the next number or not?
sum[i]= sum[i-1]+num[i] or just sum[i-1]
'''

#I am the greatest programmer.
class Solution:
    def targetSum(self,input,target):
        sum = [0 for i in range(len(input))]
        result = []
        complement = {}
        for i in range(len(input)):
            if input[i]==target:
                result.append(input[i])
            else:
                #Build dictionary before adding the next
                #check if the complement is available.

                #if complement is available, then solution is found
                #else add next number
                complement[input[i]]=target-input[i]
                for j in range(i,len(input)):
                    if complement[input[i]]==input[j]:
                        result.append(input[i])
                        result.append(input[j])
                        sum[i] = sum[i-1]
                    sum[i] = sum[i-1]+input[i]
        return result

'''
WHat is the time complexity?
worst case I go until I element before end and the complement is found
in the last element O(n)*=(n-1)~ O(n²)
What aoubt space complexity?
in worst case you need to output all the input so O(n)
'''

'''
Let's try a different solution:
A Graph approach:
'''



if __name__ == "__main__":
    input = [2,3,5]
    target = 10
    output = Solution()
    print('The output combinations is:',output.targetSum(input,target))
