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
Time Complexity: (See below)

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

//returns min. number of trials needed to fit in Formula x/(x+1)/2 = 120
//We build the 2D Table to save the preprocessing reults

int XboxDrop(int n, int k)
{
    int XboxFloor[n + 1][k + 1];
    int res;
    int xbox, floors, x;

    //initialising 1 trial for floor 1 and 0 trials for 0th floor
    for (xbox = 1; xbox <= n; xbox++) {
        XboxFloor[xbox][1] = 1;
        XboxFloor[xbox][0] = 0;
    }
    //FOr j floors and 1 Xbox we need j floors
    for (floors = 1; floors <= k; floors++)
        XboxFloor[1][floors] = floors;

    //The rest is filled with the metod written above
    for (xbox = 2; xbox <= n; xbox++)
    {
        for (floors = 2; floors <= k; floors++)
        {
            XboxFloor[xbox][floors] = INT_MAX;
            for (x = 1; x <= floors; x++)
            {
                res = 1 + max(XboxFloor[xbox - 1][x - 1],XboxFloor[xbox][floors - x]);
                if (res < XboxFloor[xbox][floors])
                    XboxFloor[xbox][floors] = res;
            }
        }
    }
    // XboxFloor[n][k] = ouput
    return XboxFloor[n][k];
}

int main()
{
    int num_xbox = 2;
    int num_floors = 120;
    cout <<  XboxDrop(num_xbox, num_floors) << endl;
    return 0;
}
