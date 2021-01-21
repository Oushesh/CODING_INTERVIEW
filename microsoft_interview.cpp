/*
Microsoft interview K closest elements:
Add Reference here and write it in C++. ##Hey Sexy!!
<<<<<<< Updated upstream
 
The first approach is to loop over points and precompute the Euclidean Distance, 
then sort it from smallest distance to largest distance: 
=======

The first approach is to loop over points and precompute the Euclidean Distance,
then sort it from smallest distance to largest distance:
>>>>>>> Stashed changes
O(nlogn)--> sort, loop once O(n)--> O(n²) order

The second approach is to try to do it in 1 go over 1 loop.
Loop --> distance(vertex, points[i])--> append distance --> closest--> append it
     --> for the first time we just append it --> performing a bool comparison sort.
     --> [min,max], if the next one >max: ignore, else: if next<min: min= next, max=min, keep doing
<<<<<<< Updated upstream
     this until the end of the vector array. 
     Time Complexity of O(n)
     Space Complexity: O(1)--> we did not redeclare any new data strucutre of size comparable
     to the array,  
=======
     this until the end of the vector array.
     Time Complexity of O(n)
     Space Complexity: O(1)--> we did not redeclare any new data strucutre of size comparable
     to the array,
>>>>>>> Stashed changes
*/
#include <iostream>
#include <vector>
#include <cmath>

<<<<<<< Updated upstream
int distance(vertex <int> &anchor, vertex<int> &point)
{
  int dist;
  dist = sqrt(abs(anchor[0]-point[0])**2+abs(anchor[1]-point[1])**2); 
=======
using namespace std;
int distance(vertex <int> anchor, vertex<int> point)
{
  int dist;
  dist = sqrt(abs(anchor[0]-point[0])**2+abs(anchor[1]-point[1])**2);
>>>>>>> Stashed changes
  return dist;
}

void swap(vector <int> a,vector <int> b)
{
  vector <int> tmp;
  tmp=a;
  a=b;
  b=tmp;
}
<<<<<<< Updated upstream
vector <int> closest(int &K, <vector vector<int>> &points, vector <int> &anchor)
{
  vector <vector <int>> K_closest;
  
  int current_dist;
=======
vector <vector<int>> closest(int K, vector <vector<int>> points, vector <int> anchor)
{
  vector <vector <int>> K_closest;


>>>>>>> Stashed changes
  //Loop over the points.
  //Perform the comparison here
  for (auto point: points)
  {
<<<<<<< Updated upstream
    current_dist = distance(anchor, point);
=======
>>>>>>> Stashed changes
    if (K_closest.size()==0)
    {
      K_closest.push_back(point);
    }
    else if (K_closest.size()==1)
    {
      K_closest.push_back(point);
<<<<<<< Updated upstream
      if (distance(anchor,K_closest[0])>distance(anchor,K_closest[1]))//TODO: complete the code & push to git
        swap(K_closest[0],K_closest[1]); 
    }
    else if (K_closest.size()==2)
    {
      if (distance(anchor,point)<distance(anchor,K_closest[0]))
=======
      int dist_min = distance(anchor,K_closest[0]);
      int dist_max = distance(anchor,K_closest[1]);
      if (dis_mint>dist_max)
        swap(K_closest[0],K_closest[1]);
    }
    else if (K_closest.size()==2)
    {
      int current_dist = distance(anchor,point);
      int dist_min = distance(anchor,K_closest[0]);
      int dist_max = distance(anchor,K_closest[1]);
      if (current_dist<dist_min)
>>>>>>> Stashed changes
      {
        vector <int> min_tmp = K_closest[0];
        K_closest[0]=point;
        K_closest[1]=min_tmp;
      }
<<<<<<< Updated upstream
      else if (distance(anchor,point)>distance(anchor,K_closest[0]) && distance(anchor,point)<distance(anchor,K_closest[1]))
=======
      else if (current_dist>dist_min && current_dist<dist_max)
>>>>>>> Stashed changes
      {
        //This is the case when "point" > min in K_closest but < max in K_closest
        K_closest[1] = point;  //overwrite max with the current point
      }
    }
  }
  return K_closest;
}

int main()
{
  int K=2;
  vector <int> anchor  = {2,3};
  vector <vector<int>> points = {{1,5},{1,2},{-1,1}};
  vector <vector <int>> K_closest = closest(points, anchor);
  //So to compute 2 closest points from points to vertex and print it out here.
  for (auto num: K_closest)
  {
    cout << "x: " << num[0];
    cout << "y: " << num[1];
  }
  return 0;
<<<<<<< Updated upstream
}
=======
}
>>>>>>> Stashed changes
