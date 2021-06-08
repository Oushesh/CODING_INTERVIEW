'''
Given a list of integers:
find the highest product you can
get from 3 of the integers.

Some constraints:
1. Check len(list)>3
2. Does the list contain only +ve numbers or not?
3. neglect 0 and 1.

2 Approaches I can think of right now:
A) Brute force build all possible multiplicaton
   possibilities of the triplets.
   Space Complextiy of O(1)
   Time Complexity of O(n³)

B) Greedy Approach.
   example = [1,2,3,47,10]
   neglect 1 and 0.
   a,b,c,d

   keep track of the triplets: [smallest,smaller,small]
   if number>smallest:
     smallest=number

Now walk the interviewer through the process:
[-10,-10,1,3,2]

1. if the triplets contain ones or zeros replace with non-ones and non-zeros
2. Check instance of -ve numbers:
   if number <0: then compare with absolute number
   otherwise compare
'''


class Integers:
    def __init__(self, numbers):
        self.numbers = numbers

    def highest_product_3(self):
        small = numbers[0]
        medium = numbers[1]
        large = numbers[2]
        triplets = [small,medium,large]

        print (triplets)
        product = small*medium*large

        neg_count = 0 #should be 0 or 1.
        for i in range(2, len(self.numbers)):
            if self.numbers[i] == 0 or self.numbers[i] == 1:
                continue

            if product<0:
                if self.numbers[i]<0:
                    if abs(self.numbers[i]) > abs(small) and abs(self.numbers[i]) < abs(medium):
                        small = self.numbers[i]
                    elif abs(self.numbers[i]) > abs(medium) and abs(self.numbers[i]) < abs(large):
                        small = medium
                        medium = self.numbers[i]
                    elif abs(self.numbers[i]) > abs(large):
                        large = self.numbers[i]
                else:

                    if self.numbers[i] > small and self.numbers[i] < medium:
                        small = self.numbers[i]
                    elif self.numbers[i] > medium and abs(self.numbers[i]) < abs(large):
                        small = medium
                        medium = self.numbers[i]
                    elif abs(self.numbers[i]) > abs(large):
                        large = self.numbers[i]

            #product +ve
            else:
                if self.numbers[i] > small and self.numbers[i] < medium:
                    small = self.numbers[i]
                elif self.numbers[i] > medium and abs(self.numbers[i]) < abs(large):
                    medium = self.numbers[i]
                elif abs(self.numbers[i]) > abs(large):
                    large = self.numbers[i]

        product = small*medium*large

        return product

if __name__ == "__main__":
    numbers = [1, 10, -5, 1, -100]
    # highest product of 3 is:
    given_numbers = Integers(numbers)
    print ('The triplets are:',given_numbers.highest_product_3())


#perform swapping here: