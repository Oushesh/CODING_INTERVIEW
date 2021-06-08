"""
Write a function which accepts a positive
integer and returns the minimum number of
steps to get to 1 assuming we can perform
the following operations:

subtract 1 from input --> x-=1

Divide by 2 if the number is divisible by 2 --> if num%mod ==0
Divide by 3 if the number is divisible by 3 --> if num%mod ==0

2*2 = 4
5 not divisibe byy or 3 -> 5-1=4
By my understanding it does not make difference:
1. at any point the number is divisble by 2 or 3:
   it does not affect the number of steps needed.
   2*3 = 6
   12 = 3*4:

Recursive approach:
"""


def steps_2_1(number, count):
    if number == 1:
        return count
    if number % 3 == 0:
        number = number // 3
    else:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number - 1
    count += 1
    # print (number,count)
    return steps_2_1(number, count)


if __name__ == "__main__":
    pos_integer = 150
    count = 0
    print(steps_2_1(pos_integer, count))
