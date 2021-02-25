/*
There is a fence with n posts, each post can be painted with one of the k colors.
You have to paint all the posts such that no more than two adjacent fence posts have the same color.
Return the total number of ways you can paint the fence.

Combination of Singlets & Doublets combination:
Singlets: factorial(n) 5*4*3*2*1
Here len(colors)=2
Doublets: RR,BB,GG,BB --> len(posts)/len(colors) --> perform permutation on each pair of cell
if len(posts)=n then doublets=factorial(n/2)
combination_number = singlet + doublet
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

      if (posts.size()%constraints.size()==0)
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

/*
n=3,
triplet each 3 of them: RRR GGG BBB permutation(for every 3 cells)
                        factorial(len(posts)/len(colors))

                        doublets, singlets, triplets.
                        factorial(len(posts))+factorial(len(posts)/len)+factorial(len(posts))
**Recursive of recursive Formulation.
if K=5, cinquets, quadruplets,triplets,duplets,singlets
factorial(len(posts))
*/
int combination_general(vector <int> posts, vector <char> colors, int constraints)
{
  //Recursive and iterative
  int output;
  int sum=1;
  vector <int> combo = {};
  //initiate the process of filling combo here:
  for (int i=0;i<combo.size();i++)
  {
    combo.push_back(0);
  }

  if (colors.size()>constraints)
  {
    while (constraints>0)
    {
      //We need to take care if division gives remainder.
      if (posts.size()%constraints==0)
      {
        output+=factorial(posts.size()/constraints);
        constraints-=1;
      }
      //Here we tackle remainder
      else
      {
        //we fill in the permutations in each cell manually.
        //Example: we fil in decreasing order until I reach 1 and again:
        for (int i=0;i<combo.size();i++)
        {
          int fillings;
          fillings = constraints;
          while (fillings>=1)
          {
            if (fillings==1)
            {
              fillings=constraints;
            }
            else
            {
              combo.push_back(fillings);
              sum*=fillings;
              fillings-=1;
            }
          }
        }
        output +=sum;
      }
    }
  }
  else
    cout << "There are not enough different colors to satisfy the constraints given"<<endl;
    return 0;
}

int main()
{
  vector <int> posts = {1,2,3,4,5,6};
  vector <char> colors = {'R','G','B'};
  int constraints = 2;
  cout << "The number of combinations is:" << combinations(posts,colors) << endl;
  cout << "The number of combination thus based on the general formula is:" << combination_general(posts,colors,constraints)<<endl;
}

//TODO: Debug and check code but I am sure its right; Code extended to general case where 
