#include <iostream>
#include <vector>
#include <map>
#include <string.h>
#include <algorithm>

using namespace std;
/*
class Solution_Breadth_First_Search{
public:
};
*/
class Solution_Dynamic_Programming{
public:
  bool wordbreak_DP(string & s, vector <string> & wordDict)
  {
      map<int,bool> cut;
      cut[0] = true;
      for (int i=1;i<s.size()+1;i++)
      {
        cut[i] = false;

        for (int j=0;j<i;j++)
        {
          //Find if the substing is found in wordDict
          if (cut[j] && find(wordDict.begin(),wordDict.end(),s.substr(j,i))!=wordDict.end())
          {
            cut[i]=true;
            break;
          }
        }
      }

      return cut[s.size()];
  }
};

int main()
{
  string s = {"catsanddog"};
  vector <string> wordDict = {"cats","dog","and","cat"};
  /*
  int i = 0;
  int j=4;
  if (find(wordDict.begin(),wordDict.end(),s.substr(i,j))!=wordDict.end())
  {
      cout << "target found" << endl;
  }
  */
  Solution_Dynamic_Programming output;
  cout << output.wordbreak_DP(s,wordDict)  << endl;
  return 0;
}

//To check this problem here
//TODO write the Breadth first search and depth first search here
//as well
