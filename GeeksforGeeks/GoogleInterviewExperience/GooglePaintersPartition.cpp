/*
We have to print n boards of length {A1,A2,...An}.
There are k painters available and each takes 1 unit of time
to paint 1 unit of board. --> 1 unit of Board Length = 1 unit of time.

The problem is to find the minimum time to get this job done under the
constraints that any painter will only paint continuous sections of
boards, say board {2,3,4} or only board {1} or nothing but board {2,4,5}.

EXAMPLE:

It is obvious that the strategy of dividing the boards into k equal
partitions won't work for all the cases. We can observe that the problem
can be broken down into: Given an array A of non-negative integers and
a positive k, we have to divide A into k of fewer partitions such that
the maximum sum of the elements in a partition, overall partitions is
minimized.

For example:
 k = 2, A = {10, 20, 30, 40}
if partition = 1:
so time=100 max_sum(A)=100

if partition = 2:
    10, 20,30,40 max(90)
    10,20,30,  40 max(60)

min(100,90,70,60)=60

Lets say T(n,k)
T(1,1)
T(1,2)
T(1,3)
General Formula:  min(max(T(i,Ki-1),sum(A1,--An)))

n = length of the array
k: number of constraints or divisions.
              T(4,3)
          /     \        \
        T(1,2) T(2,2)  T(3,2)
          /      /         /
        T(1,1)     T(1,1)   T(1,1)
*/

/*
Using real of dynamic programming in for this problem
*/

#include <iostream>
#include <vector>
#include <climits>

using namespace std;
//int sum(int arr[], int start,int end)
int sum(vector<int> vec, int start,int end)
{
  int total = 0;
  for (int i=start; i<=end;i++)
    total+=vec[i];
  return total;
}

//bottom up tabular dp
int findMax(vector <int> vec, int n, int k)
//int findMax(int arr[], int n, int k)
{
  //initialize table with size k*n
  //Space Complexity here K*n
  int dp[k+1][n+1] = {0};

  //base cases
  //k=1
  for (int i=1;i<=n;i++)
    dp[1][i] = sum(vec,0,i-1); //recursively add the pervious ones

  //n=1
  for (int i=1; i<=k; i++)
    dp[i][1]=vec[0];

  //2 to k partitions
  //2 to n boards
  for (int i=2;i<=k;i++)
  {
    for (int j=2; j<=n;j++)
    {
      //trace minimum
     int best = INT_MAX;
     for (int p=1; p<=j; p++)
     {
       best = min(best,max(dp[i-1][p],sum(vec,p,j-1)));
       dp[i][j] = best;
     }

    }
  }
  return dp[k][n];
}

// driver function
int main()
{
  //if this would be a vector we could this more neat
  vector <int> vec = {10,20,60,50,30,40};
  int n = vec.size();

  //int arr[] = {10,20,60,50,30,40};
  //int n = sizeof(arr)/sizeof(arr[0]);
  int k = 3;
  cout << findMax(vec,n,k) << endl;
  return 0;
}

//TODO: perform the same operation using the vectors operation
//DONE: vectors.
