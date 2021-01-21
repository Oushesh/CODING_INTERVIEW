/*
Reference: https://practice.geeksforgeeks.org/problems/x-total-shapes3617/1/?company[]=Amazon&amp;company[]=Amazon&amp;page=1&amp;query=company[]Amazonpage1company[]Amazon
###This a coding interview similar to 0s and 1s of DFS problem


1. Use a combination of greedy and search/graph problem: -->
   1. Loop over the grid & spot the first:
      Lets say we count X->1, 0->0

      We loop over the neighbours &
*/
#include <iostream>
#include <vector>

using namespace std;

//A different style of solving it is to feed (i,j)--> output the neighbours
//as 4 tuples of the vector data structure then for all neighbour in neighbours:
//perform the 4 function calls.

void neighbours(vector <vector<int>> &grid,int i, int j, int m, int n)
{
  if (i<0 || j<0 || i>m || j>n || grid[i][j]!=1)
    return;

  //once we are in the function:
  //each time when we start we can perform recursive call.
  grid[i][j]=0;

  neighbours(grid,i+1,j,m,n);
  neighbours(grid,i-1,j,m,n);
  neighbours(grid,i,j+1,m,n);
  neighbours(grid,i,j-1,m,n);
}

int count(vector<vector<int>> &grid)
{
  int count = 0;
  int m = grid.size();
  int n = grid[0].size();

  //Loop over the whole grid.
  for (int i=0;i<m;i++)
  {
    for (int j=0;j<n;j++)
    {
      if (grid[i][j]==1)
        {
          neighbours(grid,i,j,m,n);
          count+=1;
        }
    }
  }
  return count;
}

//The number of islands 1s is 3.
int main()
{
  vector<vector<int>> grid = {{1,0,1},{0,1,0},{1,1,1}};
  cout << "ABC";
  cout << "The number of islands is:" << count(grid);
  return 0;
}
