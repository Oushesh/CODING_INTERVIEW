/*
Ref: https://www.geeksforgeeks.org/allocate-minimum-number-pages/

Given number of pages in n different books and m students.
The books are arranged in ascending order of number of pages.
Every student is assigned to read some consecutive books. The
task is to assign books in such a way that the maximum number
of pages assigned to a student is minimum.

n - books [1,2,...n]
m - students

Way 1: Dynamic Programming Build a precomputed matrix
Way 2: BInary Search.

If k=2 we can do binary search. -->
everything that lower than the mid can be on the left

i) mid,
ii) left,
iii) right,

*/

#include <iostream>
#include <vector>
#include <assert.h>
#include <climits>

//assert is used to find if there a condition is true
using namespace std;
//Utility Function to check fi current
//minimum value is feasible or not.

bool isPossible(vector <int> books,int n, int m, int curr_min)
{
  int studentsrequired = 1;
  int curr_sum = 0;

  //iterate over all books
  for (int i=0;i<n;i++)
  {
    //Check if current number of pages are greater
    //than curr_min that means we will get the result
    //after mid num. of pages
    if (arr[i]>curr_min)
      return false;

    //count how many students are required to distribute
    //curr_min pages
    if (curr_sum + arr[i]> curr_min)
    {
      //increment student count.
      studentsRequired++;
      //update curr_sum
      curr_sum = arr[i];
      //if students required becomes
      //greater than given number of students
      if (studentsRequired>m)
        return false;
    }
    else
      curr_sum+=arr[i];
  }
  return true;
}

int findMinPages(vector <int> & pages, int m, int n)
{
  sum = 0;
  assert(m>n);

  //Count total number of pages.
  for (int i=0;i<n;i++)
    sum+=vec[i];

  int start=0;
  end=sum;
  int result = INT_MAX; //C++ limits

  //Binary Search, start, end part of the the array
  int start = 0;
  int end = pages.size();
  //traverse until we reach the end. start move to the right, end to the left.
  //traverse:
  while (start<=end)
  {
    //check if its possible to distribute books by using mid
    //as current minimum.
    int mid = (start+end)/2;
    if (isPossible(books,n,m,mid))
    {
      //if yes then find the minimum distribution
      result = min(result,mid);
      end = min-1;
    }
    else
        //if not possible means pages should be
        //increaed so update start = mid+1
        start = mid+1;
  }
  //at last return min. pages
  return result;
}

int main()
{
  //number of pages in the book
  vector <int> books = {12,34,67,90};
  int n = books.size(); //number of books here.
  int m = 2; //number of students
  cout << "The minimum required number of pages is:" << findMinPages(books,n,m)<< endl;
  return 0;
}

//Let's walk the interviewer through the experience here:

//Take this example: [12,34,45,67,90]
//First iteration of Binary Search:
//Lets say k=2., we need just to split the array into 2.
//Just normal Binary Search

//mid <high, lower <mid-> if not swap the numbers.


//Lets say array = [12,34,45]
//mid = 34, low= 12, high --> keep track of the cur_mid=34

//The big thing is how to connect the

/*
'''
[12,34,45,90,47,89,2,1], K=4

1.K=1--> (all array)= (sum(array)),
//K=2, all possibilities: [12| 34,45,90,47,89,2,1]->max of all the possibilities here.

'''
*/
