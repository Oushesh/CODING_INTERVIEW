/*
There is a fence with n posts, each post can be painted with one of the k colors.
You have to paint all the posts such that no more than two adjacent fence posts have the same color.
Return the total number of ways you can paint the fence
*/

#include <iostream>
#include <vector>

using namespace std;

//I prefer the recursive implementation. To hell with iterative

int sum(vector <int> vec)
{
  int sum=0;
  for (auto &a:vec)
    a+=sum;
  return sum;
}
int factorial(int n)
{
  if (n==1)
    return n;
  return n*factorial(n-1);
}

int combinations(vector <int> posts, vector <char> colors)
{
  int combo;
  if (posts.size()%2==0)
  {
    int doublet = factorial(posts.size()/2);

    if (posts.size()%colors.size()==0)
      int singlets = factorial(colors.size())*posts.size()/colors.size();
    else
    {
      vector <int> singlets = {};
        int start = colors.size();
        for (int i=0;i<posts.size();i++)
          if (start==1)
            start = colors.size();
          singlets.push_back(start);
          start-=1;
        //sum of elements in vector
        int singlet = sum(singlets);
    }
  }
  else
  {
      int singlet;
      vector <int> singlets = {};
      int doublet = factorial(int(posts.size())/2)*(colors.size()-1);

      if (posts.size()%colors.size()==0)
      {
        singlet = factorial(colors.size())*(posts.size()/colors.size());
      }
      else
      {

        int start = colors.size();
        for (int i=0;i<posts.size();i++)
          if (start==1)
            start = colors.size();
          singlets.push_back(start);
          start-=1;
        //sum of elements in vector
        int singlet = sum(singlets);
      }
      combo = int(singlet+doublet);
  }
  return combo;
}

int main()
{
  vector <int> posts = {1,2,3,4,5,6};
  vector <char> colors = {'R','G','B'};
  int constraints = 2;
  cout << "The number of combinations is:" << combinations(posts,colors) << endl;
}
