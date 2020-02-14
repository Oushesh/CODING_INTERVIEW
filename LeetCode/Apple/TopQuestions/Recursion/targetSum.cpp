#include <iostream>
#include <map>
#include <vector>

using namespace std;
class Solution
{
public:
  vector <int> targetSum(vector <int> & input, int & target)
  {
    vector <int> sum;
    for (int i=0;i<input.size();i++)
    {
      sum[i]=0;
    }
    vector <int> result;
    map <int,int> complement;
    for (int i=0;i<input.size();i++)
    {
      if (input[i]==target)
      {
        result.push_back(input[i]);
      }
      else
      {
        complement[input[i]]=target-input[i];
        for (int j=i;j<input.size();j++)
        {
          if (complement[input[i]]==input[j])
          {
            result.push_back(input[i]);
            result.push_back(input[j]);
            sum[i] = sum[i-1];
          }
          else
          {
            sum[i] = sum[i-1]+input[i];
          }
        }
      }
    }
    return result;
  }
};

int main()
{
  vector <int> input = {2,3,5};
  int target = 10;
  Solution output;
  output.targetSum(input,target);
  //cout << output.targetSum(input,target)[1] << endl;
  return 0;
}
