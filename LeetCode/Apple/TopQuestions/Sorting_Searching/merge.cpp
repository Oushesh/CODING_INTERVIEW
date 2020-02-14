#include <iostream>
#include <map>
#include <vector>
#include <functional>
#include <algorithm>

using namespace std;

class Solution{
public:
  vector<vector<int> > merge(vector<vector<int> > & intervals)
  {
    //sort the intervals based on the first value
    // sort using a lambda expression
    sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b)
    {
            return a[0] > b[0];
    });
    int n;
    vector <vector <int>> merged(n);
    for (int i=0;i<intervals.size();i++)
    {
      if (merged.size()==0|| (merged[-1][1] < intervals[i][0]))
      {
        merged.push_back(intervals[i]);
      }
      else
      {
        merged[-1][1]= max(merged[-1][1],intervals[i][1]);
      }
      return merged;
    }
  }
};

int main()
{
  vector<vector<int> > intervals = {{1,3},{2,6},{8,10},{15,18}};
  Solution output;
  //cout in c++ does not print all of them
  //do elementwise print
  vector <vector<int>> merged;
  merged=output.merge(intervals);
  for (int i=0;i<merged.size();i++)
  {
    for (int j=0;j<merged[i].size();j++)
    {
      cout << merged[i][j] << endl;
    }
  }
  return 0;
}
