//https://www.youtube.com/watch?v=tOD6g7rF7NA

#include "stdio.h"
#include <algorithm>
#include <map>

string s = "3145926535897946262433832789"
string target = {"3","314", "31", "59", "49", "9001", "159265897"}

//Thought Patterns:

/*
AIM: To find minimum splits.

Lets try 2 pointers approach. 1 starting from the beginning and one from the right.
loop over just once. Time Complexity of: O(n), Space Complexity: O(1)
space_count = 0

1. 3145926535897946262433832789
2. 3 145926535897946262433832789 --> 0:left     right:len(s)
	check(left_sub,right_sub) in target: --> return count
	else:
	  left+=1
	  check(31,45926535897946262433832789)

	  now what happens if we have both 31 and 314, well does not matter as
	  long as the remaining subarray is also inside the target. it does
    not affect the overall subarray count.

    we can stop.

    if not both subarrays in target:
      try left+=1
          right-=1

	else:
		prefix in subarry: suffix not
		it means 2 posibilites: or part of the suffixes is in subarray ---> recursive function call here.
	     nocheck(x)

while (left<=right)

if string[0:left] and string[left+1:right] in target:
	else:
	left
	if (string[0:])
		left+=1
		right-=1
	return count
check(s,target)


*/

class String_Check
{

}

int main()
{
	string s = "3145926535897946262433832789";
	string target =
	return 0;
}
