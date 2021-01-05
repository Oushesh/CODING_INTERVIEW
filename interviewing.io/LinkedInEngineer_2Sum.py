'''
Reference: https://www.youtube.com/watch?v=JtIYZKsxswA
'''

'''
There are different approaches here:
Since we are mentionning about 2 sum:
If we brute force the problem we have
a complexity
'''

class Numbers:
    def two_sum(self,numbers,target):
        complement = {}
        for number in numbers:
            if number < target:
                complement[number] = target - number
                if complement[number] in numbers:
                    return number, complement[number]

if __name__ == "__main__":
    nums = [3,6,9,12,15,4,2,1,30]
    target = 15
    object = Numbers()
    print ('The 2 pair sum is:', object.two_sum(nums,target))
