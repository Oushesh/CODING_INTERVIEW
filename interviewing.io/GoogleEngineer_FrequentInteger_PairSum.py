'''
Reference: https://interviewing.io/recordings/Java-Google-13
'''

class Integer():
    def frequency(self,numbers):
        counter = {}
        for number in numbers:
            if number not in counter:
                counter[number]=1
            else:
                counter[number]+=1
        return counter

    def search_most_frequent(self,numbers):
        '''
        Return the key from counter,
        whose value is highest.
        '''
        counter = self.frequency(numbers)
        most_frequent=max(counter.values())
        for key,value in counter.items():
            if value == most_frequent:
                return key

    '''
    The second question asks about
    printing out pairs of numbers in
    an array that sum to N
    '''

    def complement(self,numbers,sum):
        complement = {}
        for number in numbers:
            complement[number]= sum-number
        return complement
    '''
    The idea of 2 pointers, is to consider
    1 number if it is less than the sum.
    '''
    def pair2sum_pointers(self,numbers,sum):
        for i in range(len(numbers)-1):
            if numbers[i] < sum:
                #Loop to find the complement
                for j in range(i,len(numbers)):
                    if numbers[i]+numbers[j]== sum:
                        return [numbers[i],numbers[j]]
    '''
    To find the pair of numbers summed
    to N, we loop over the list:numbers:
    check if the complement also exists.
    '''
    def pair2sum_complement(self,numbers,sum):
        complement = self.complement(numbers,sum)
        print (complement)
        #for number in numbers:
        for number in numbers:
            #check if the complement exist in the numbers
            if complement[number] in numbers:
                return [number,complement[number]]

    '''
    Find the only integer that only
    appear once in an array in constant space
    and O(n) time.
    '''
    def integer_appear_once(self,numbers):
        frequency = {}
        for number in numbers:
            if number not in frequency:
                frequency[number]=1
            else:
                frequency[number]+=1
        print (frequency)
        return number


if __name__ == "__main__":
    numbers = [2,2,4,5,4,7,9]
    sum     = 13
    solution = Integer()
    print (solution.pair2sum_pointers(numbers,sum))
    print (solution.pair2sum_complement(numbers,sum))

    print (solution.search_most_frequent(numbers))

    numbers2 = [2,3,3,5,3,5,2,4]
    '''
    we expect 4 which appears only once.
    Now if we assume, we only 1 digit that
    appears only once and this is unique,
    the first time we have 1 digit whose
    count is one we can stop. Worst case,
    this will appear in the end of the list.
    '''
    print ('The unique number that appear only once',solution.integer_appear_once(numbers2))
