#include <vector>
#include <algorithm>   // for std::sort
#include <functional>  // for std::greater
#include <iostream>

class Solution
{
public:
  KClosest(std::vector<std::vector<int>>  points)
  {
    return std::sort(points.begin(), points.end(), std::greater<std::vector<int>>());
  }
};

int main()
{
  // Set up an example vector
  int K = 2;
  Solution object;
  std::vector<std::vector<int>> points{{3,3},{5,-1},{-2,4}};
  std::cout << object.KClosest(points) << std::endl;
  /*
  std::vector<std::vector<int>> v{{5, 9, 4, 12, 4},
                                  {7, 9, 3, 4, 7, 9},
                                  {6, 5, 11},
                                  {5, 8, 7, 3},
                                  {5, 9, 5, 1, 1}};

  // Perform the sort
  std::sort(v.begin(), v.end(), std::greater<std::vector<int>>());

  // Output the results
  for (const auto& i : v)
  {
    for (auto j : i)
      std::cout << j << " ";
    std::cout << "\n";
  }
  */
}
