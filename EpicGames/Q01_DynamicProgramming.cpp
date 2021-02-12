//Dynamic Approach to the problem:

/*
The dynamic problem approach is used
to make a lookup table and to avoid
calculating the answers again and again.

The use of the lookup talbe is as follows:

xbox--> number of xboxes given
floor--> number of floors.

How to fill the talbe?
For 1 Xbox --> the number of attempts= number of floors (120)
For 2 Xboxes --> Floor1 + max(0,DP[1][1])
                 Floor2 + max(DP[1][1],0)
                 DP[2][2] = minimum(0,DP[1][1],1+max(DP[1][1],0))
                 .
                 .
                 .

Space Complexity: Owing to building the table: O(Xbox*Floors), saving varialbes
                  amount to Order of 1 and in Big (O) Notation: O(Xbox*floors)
Time Complexity:
*/
#include <limits.h>
#include <iostream>
using namespace std;

int max(int a, int b)
{
  if (a>b)
    return a;
  else
    return b;
}

/* Function to get minimum
number of trials needed in worst
case with n eggs and k floors */

//returns min. number of trials needed to fit in Formula x
int XboxDrop(int n, int k)
{
    /* A 2D table where entery
    eggFloor[i][j] will represent
    minimum number of trials needed for
    i eggs and j floors. */
    int XboxFloor[n + 1][k + 1];
    int res;
    int xbox, j, x;


    //initialising 1 trial for floor 1 and 0 trials for 0th floor
    for (xbox = 1; xbox <= n; xbox++) {
        XboxFloor[xbox][1] = 1;
        XboxFloor[xbox][0] = 0;
    }

    // We always need j trials for one egg
    // and j floors.
    for (j = 1; j <= k; j++)
        XboxFloor[1][j] = j;

    // Fill rest of the entries in table using
    // optimal substructure property
    for (xbox = 2; xbox <= n; xbox++)
    {
        for (j = 2; j <= k; j++)
        {
            XboxFloor[xbox][j] = INT_MAX;
            for (x = 1; x <= j; x++)
            {
                res = 1 + max(XboxFloor[xbox - 1][x - 1],XboxFloor[xbox][j - x]);
                if (res < XboxFloor[xbox][j])
                    XboxFloor[xbox][j] = res;
            }
        }
    }

    // eggFloor[n][k] holds the result
    return XboxFloor[n][k];
}

/* Driver program to test to pront printDups*/
int main()
{
    int xbox = 2;
    int floors = 120;
    cout <<  XboxDrop(xbox, floors) << endl;
    return 0;
}
