#Referecne: https://interviewing.io/recordings/CSharp-Microsoft-5/
'''
Partition a list with a given value K, such
that values in the list less than K are to
the left to K and values in the list than
K are to the right of K.
'''

'''
Thought Patterns:
list = [5,4,1,6,7,9] #[1,4,5,6,7,9]
list2 = [1,5,4,7,6,9] #[1,4,5,7,6,9]


FInd K in the list:
Go to K
if left > K ,swap(number[left],K)
if right <K, swap(number[right],K)
Loop for this process over all the
elements.
'''

class List:
    def sort(self,list,K):
        if K in list:
            for i in range(len(numbers)):
                if numbers[i]==K:
                    left  =
                    right =

        return sorted


if __name__ == "__main__":
    list = [5,4,1,6,7,9] #[1,4,5,6,7,9]
    list2 = [1,5,4,7,6,9] #[1,4,5,7,6,9]

    K = 5
    givenList = List()
    print ('sorted',givenList.sort(list))
