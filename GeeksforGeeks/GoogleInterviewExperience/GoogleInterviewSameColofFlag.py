'''
Ref: Dutch Flag Problem

Algorithm was first proposed by dijska. Great Guy!!

Given an array representing an unsorted Flag of colours.
Red-0
Blue-1
White-2

For example: list=[0,1,2,2,2,0,0,0,1,1], total_number = 10

3 different inputs: freq(0): 4
                    freq(1): 3
                    freq(2): 3
Typical output: [0]


We aim to solve this problem in 1 go and we dont know the number of
different elements in the list. len(set(list))==3 --> we get it


Lets say we dont.
unique = []

1.Loop over the array.
2. if len(unique)==0: add list.append(array[0]), idx = 0
3. if next one is not in unique --> differs. new_idy = 1
4. When I encounter no new element --> 2,2,2,
   [0,1,2,2,2,0,0,0,1,1]
   idx_0_start = 0, idx_0_end = None, idx_1_start = 1, idx_1_end = None
   idx_2 = 3,4,5 ---> idx_2_start = 3, idx_2_end = 5

   We encouter 0: idx_start is not None(encountered before)--> swap(idx_start_end,idx_1_end)
    idx_0_start = 0, idx_0_end = 1, idx_1_start = 5, idx_1_end = None
    idx_2 = 3,4,5 ---> idx_2_start = 3, idx_2_end = 5

    [0,0,2,2,2,1,0,0,1,1] --> [0,0,0,0,2,2,2,1,1,1]
'''

class DutchFlag():
    def unique_color(self,colors):
        return len(set(colors))

    def sort(self,colors):
        unique = []
        i_start, i_end, j_start, j_end, k_start, k_end = None #TODO: find an automatic way to declare the variables here #we assume we found the 3 unique colours.

        #TODO: we know we have 3 colours
        i = 0
        j = 1
        k = 2

        while i<len(colors) or j<len(colors) or k<len(colors):
            while colors[i]==colors[i+1]:
                if colors[i] not in unique:
                    unique.append(colors[i]) #Keep track of the visited items so far.
                #keep looping as long as the next one is the same
                i+=1



#TODO: Check all code in the google interview experience journey.







if __name__ == "__main__":
    input_flag = [0,1,2,2,2,0,0,0,1,1]
    print ('The resultant is')
