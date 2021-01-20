/*
Reference: https://practice.geeksforgeeks.org/problems/x-total-shapes3617/1/?company[]=Amazon&amp;company[]=Amazon&amp;page=1&amp;query=company[]Amazonpage1company[]Amazon
###This a coding interview similar to 0s and 1s of DFS problem


1. Use a combination of greedy and search/graph problem: -->
   1. Loop over the grid & spot the first:
      Lets say we count X->1, 0->0


      We loop over the 
*/
#include <iostream>
#include <vector>
#include <arithmetic>

using namespace std;


int count(vector<vector<int>> &grid)
{
  count = 0;

  neighbours(int i, int j);
  return count;

}


int main()
{
  vector<vector<int>> grid = {{1,0,1},{0,1,0},{1,1,1}};
  cout << "The number of islands is:" << count(grid) << endl;
  return 0;
}
