#https://interviewing.io/recordings/Python-interviewing.io-1/

'''
1) Write a function that takes a string as an input
and returns a shuffled version of that string.
(i.e. a version where each character is just as likely to be
in any given position)

2) Write a function that analyzes how well your previous function
randomly shuffles the string.
How do this? Bernoulli Experiments.
The idea is to run shuffle len(string) times and check
how different the results are from 1 another
'''

import random
import math
class Item():
    def shuffle(self,string):
        '''
        shuffle index, keep track of the picked index.
        shuffle and pick randomly from the remining indices
        '''
        random_index = int(random.random()*len(string))
        picked = []
        output = []
        while (len(output)<len(string)):
            if random_index not in picked:
                picked.append(random_index)
                output.append(string[random_index])
            else:
                random_index = int(random.random()*len(string))
        return output

    def shuffle_python(self,string):
        random.shuffle(string)
        return string

    def check_shuffle(self,string):
        '''
        All the individual lists have to be
        different from each other. So we have
        to check each possible pairs. Time Complexity
        is thus: O(n²).
        '''
        shuffle_experiments = [] #List of Lists
        for i in range(len(string)):
            shuffle_experiments.append(self.shuffle(string))
        '''
        Metric Calulation
        if we have len(string)=n
        then number of combinations for checking, nC2:
        metric = different/nc2
        '''
        count = 0
        for i in range(len(shuffle_experiments)-1):
            for j in range(i,len(shuffle_experiments)):
                if not shuffle_experiments[i] == shuffle_experiments[j]:
                    print (shuffle_experiments[i],shuffle_experiments[j])
                    count +=1
        return count/len(shuffle_experiments)


if __name__ == "__main__":
    string = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
    currentItem = Item()
    shuffled = currentItem.shuffle(string)
    print (shuffled)
    print (currentItem.shuffle_python(string))

    print (currentItem.check_shuffle(string))
