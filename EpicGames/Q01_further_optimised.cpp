#include <iostream>
using namespace std;

/*
This approach is based on Bernoulli Equation
Check the equations on wiki.

Idea:
Xbox Dropped --> Breaks --> (x-1) trials + (n-1) Xboxes
             --> Not break --> (x-1) trials + X Xboxes

Let maxFloors (x, n) be the maximum number of floors
that we can cover with x trials and n Xboxes.
maxFloors(x, n) = maxFloors(x-1, n-1) + maxFloors(x-1, n) + 1
For all x >= 1 and n >= 1

Best:
No Floor covered with O Xboxes and O floors
maxFloors(0, n) = 0
maxFloors(x, 0) = 0

We need to cover numFloor Floors:
maxFloors(x, n) >= numFloors.
maxFloors(x, n) = &Sum;xCi
                  1 <= i <= n   ----------(2)

&Sum;xCj  >= k ---> Wikipedia (Binoamial coefficient)
1 <= i <= n

AIM: find min value of X which satisfies the above inequality.
We use Binary Search
*/


// Find sum of binomial coefficients xCi
// (where i varies from 1 to n).
int binomialCoeff(int x, int n)
{
    int sum = 0, term = 1;
    for (int i = 1; i <= n; ++i) {
        term *= x - i + 1;
        term /= i;
        sum += term;
    }
    return sum;
}

//Binary Search
int minTrials(int n, int k)
{
    //Low is the first floor,
    //high is the toppest floor (120)
    int low = 1;
    int high = k;

    //Classical Binary Search
    while (low < high) {
        int mid = (low + high) / 2;
        if (binomialCoeff(mid, n) < k)
            low = mid + 1;
        else
            high = mid;
    }
    return low;
}

//The main gives the minnumber of trials (starting):
//Again we do the same as with the Dynamic Programming Approach:
//insert the value: 15 into x(x+1)/2=120 to get all the possible floors
//Ans: [15,29,42,54,65,75,84,92,99,105,110,114,117,119,120]

//Space Complexity: We are not sotring anything apart from variables: O(1)
//Time Complexity:  We are doing Binary Search over number of floors: O(num_Xboxlognum_Floors)


int main()
{
  int num_Xbox = 2;
  int num_Floors = 120;
  cout << "The minimum number of trials is:" << minTrials(num_Xbox, num_Floors) << endl;
  return 0;
}
