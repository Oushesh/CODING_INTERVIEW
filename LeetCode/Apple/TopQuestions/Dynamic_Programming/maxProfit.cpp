#include <iostream>
#include <vector>
#include <limits>


using namespace std;
class Solution{
public:
  int maxProfit (vector <int> & prices)
  {
    if (prices.size()<2)
    {
      return 0;
    }
    int max_profit = numeric_limits<int>::lowest();
    int buy        = prices[0];
    int profit;
    for (int d=1;d<prices.size();d++)
    {
      if (prices[d]<buy)
      {
        buy = prices[d];
      }
      profit = prices[d]-buy;
      if (profit > max_profit)
      {
        max_profit = profit;
      }
    }
    return max_profit;
  }
};

int main()
{
  vector <int> prices = {7,15,3,6,4};
  Solution output;
  cout << output.maxProfit(prices) << endl;
  return 0;
}
