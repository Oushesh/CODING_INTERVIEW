/*
The same code as written in python. we write in .cpp
*/

#include <iostream>
#include <vector>

#include <deque>

using namespace std;

class CoinGame
{
public:
  deque <int> coins;
  char turn;
  deque <int> user;
  deque <int> opponent;
  int current;

  //Constructor
  CoinGame(deque <int> coins)
  {
    this->coins = coins;
    this->turn = NULL;
    this->user = {};
    this->opponent = {};
    this->current = NULL;
  }
};

bool comparator(int a, int b)
{
  return (a<b);
}
int count(CoinGame Game)
{
  CoinGame Game;
  Game.turn = "u";

  while (coins.size()>0)
  {
    if (coins[0]>coins[coins.size()-1])
      Game.current = coins.pop_front();
    else
      Game.current = coins.pop_back();

    if (Game.turn == "u")
    {
      Game.user.push_back(Game.current);
      Game.turn = "o";
    }
    else if (Game.turn == "o")
    {
      Game.opponent.push_back(Game.current);
      Game.turn = "u";
    }

    return max(accumulate(self.user.begin(),self.user.end(),0.0),accumulate(self.opponent.begin(),self.opponent.end(),0.0))
  }
}

int main()
{
  vector <int> coins = {8,15,3,7};
  CoinGame game;
  cout << "The max count of the number of coins is:" << count(coins) << endl;
  return 0;
}

//TODEBUG: Here to debug the code needed
