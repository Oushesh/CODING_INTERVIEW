/*
You are given N blocks of height 1…N. In how many ways can you arrange these
blocks in a row such that when viewed from left you see only L blocks
(rest are hidden by taller blocks) and when seen from right you see
only R blocks? Example given N=3, L=2, R=1 there is only one arrangement
{2, 1, 3} while for N=3, L=2, R=2 there are two ways {1, 3, 2} and {2, 3, 1}

Height: 1,2,3, {2,1,3}
N=3, L=2, R=1

int output-> how many ways. (count)
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <cassert>

using namespace std;
class Arrangement
{
  public:
    int L;
    int R;
    vector <int> blocks;
    //Constructor
  Arrangement(int L,int R, vector <int> blocks)
  {
    this->L = L;
    this->R = R;
    this->blocks = blocks;
  }
};

int permute_iterative(int & num_constraint)
{
  /*
  return number of permutations
  */
  int number = num_constraint;
  int output;
  while (number>0)
  {
    output = number*number-1;
    number -= number;
  }
  return output;
}

int permute(int num_constraint)
{
  if (num_constraint==1)
    return num_constraint;
  return num_constraint*permute(num_constraint-1);
}

int rearrange(vector <int> blocks,int & L, int & R)
{
  int minimum=min(L,R);
  int second = max(L,R);
  second -=1;
  int num_constraint = blocks.size()-(minimum+second);
  int permutations = permute(num_constraint);
  return permutations;
}

int main()
{
  int L = 2;
  int R = 1;
  vector <int> blocks = {1,2,3,4,5,6};
  Arrangement current(L,R,blocks);
  cout << "The number of combinations is:" << rearrange(blocks,L,R)<< endl;
}

//TODO: use cassert to write tests.
//TODO: To check and send jadaav this assignment
