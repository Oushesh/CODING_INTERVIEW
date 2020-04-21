'''
#Coding Interview Microsoft Engineer: Max Consecutive Sequence
Reference: https://www.youtube.com/watch?v=XXLVi2y2GrY
'''

'''
Notes: Given a list of integers L,
find the maximum length of sequence
of consecutive numbers that can be
formed using elements from L:
#[5,2,99,3,4,1,100] --> max(99,100), [|1..5|]

1. First approach sort then go over it --> O(nlogn)
2. Move over the sequence and check if the next one is incremented by 1
'''

'''
1. Can we do better?
2. Yes. Some sort of dynamic sorting and moving the elements at once
'''

class Sequence:
    def max_sequence_sorting_approach(self,sequence):
        '''
        This approach is about sorting the sequence. O(nlogn)
        define start_index = 0
        end_index = 1
        check if next number is current +1. the irst time the
        condition becomes false --> Break --> return start_index, end_index
        '''
        sorted_sequence = sorted(sequence) #O(n)logn approach since we are sorting first
        print (sorted_sequence)
        output_sequence = []
        start = 0
        i = 0
        j = 1
        for _ in range(len(sequence)):
                while (sorted_sequence[j]==sorted_sequence[i]+1):
                    i+=1
                    j+=1
                end = j
                output_sequence.append(sorted_sequence[start:end])
        return max(output_sequence)
    '''
    Now interviewer asks me can I do better?
    Well, maybe. Lets see if we can do it O(n)
    time complexity approach
    [5,2,99,3,4,1,100]
    We avoid sorting first
    So lets's say instead:
    anchor point = min of elements sofar.
    5,2 : [5,4,3,2]  --> list all numbers from 5 to 2 incl. 2
    99 > len(99-2) > len(list) neglect
    3 in the list defined
    4 in list defined
    1 is not in list defined, but 1 is 1 less than min, which is 2
    #Perform consecutiveness check between the 2 barriers.
    100> len(100-1): so neglect
    '''

    '''
    Now lets code this.
    '''
    def max_sequenece_dynamic_approach(self,numbers):
        minsoFar = 0
        anchor = numbers[0]
        for number in numbers:
            if abs(anchor-number) < len(numbers):
                if number < minsoFar:
                    minsoFar = number
                    '''
                    Now, build the list in between the 2 boundaries.
                    '''
        return None
    '''
    Visited nodes: Set to if false at the beginning.
    Perform consecutive search if the next item is in the list
    Perform also Backwards search.
    Perform
    '''
    def max_sequence_BFS_approach(self,numbers):
        '''
        set visited as a dictionary at the beginning
        '''

        visited = {number:0 for number in numbers}
        length = 0
        set_numbers = set(numbers)
        current_length = 0

        for i in range(len(numbers)):
            forward_num = numbers[i]
            backward_num = numbers[i]
            '''
            Check for forward number if it is in the array.
            '''
            while forward_num in set_numbers and not visited[forward_num]:
                visited[forward_num]=1
                forward_num+=1 #Update the number by each time and look for it   #in the set.
                current_length+=1
            '''
            Check for backward number if it is in the array.
            Update if the number was already visited. Get
            the index value based on the
            '''
            while backward_num in set_numbers and not visited[backward_num]:
                visited[backward_num]=1
                backward_num-=1
                current_length+=1
        return max(length,current_length)

    '''
    Lets use the idea of HashSet or Set for O(1) look up time
    '''
    def max_sequence_HashSet(self,numbers):
        length = 0
        set_numbers = set(numbers)

        for number in numbers:
            if number-1 not in set_numbers:
                current_length = 0
                current_num = number
                '''
                now find the forward consecutive numbers
                '''
                while current_num in set_numbers:
                    current_num +=1
                    current_length+=1
                max_length = max(current_length,length)
        return max_length


if __name__ == "__main__":
    numbers = [5,2,99,3,4,1,100]
    current_Seq = Sequence()
    max_sequence = current_Seq.max_sequence_sorting_approach(numbers)
    print ('max consecutive sequence is:',max_sequence)
    print('max consecutive sequence of length is:', current_Seq.max_sequence_HashSet(numbers))

    print ('max consecutive sequence',current_Seq.max_sequence_BFS_approach(numbers))
