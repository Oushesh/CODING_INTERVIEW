#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;
class Solution
{
public:
  vector <string> generateParenthesis(int N)
  {
    vector <string> output;
    vector <string> S;
    vector <string> result;
    int open = 0;
    int closed = 0;
    result = backtrack(output,N,S.push_back("("),open+1,closed);
    return result;
  }
  vector <string> backtrack(vector <string> output,int N,vector <string> S,int open, int closed)
  {

    if (S.size()==2*N)
    {
      output.push_back(S);
    }
    if (open <N)
    {
      //how to add strings in C++?
      output=backtrack(output,N,S.push_back("("),open+1,closed);
    }
    if (closed < open)
    {
      output=backtrack(output,N,S.push_back(")"),open,closed+1);
    }
    return output;
  }
};
int main()
{
  int N = 3;
  Solution output;
  output.generateParenthesis(N);
  return 0;
}
