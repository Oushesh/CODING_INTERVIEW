/*
#Reference: https://www.geeksforgeeks.org/minimum-number-of-nodes-to-be-removed-such-that-no-subtree-has-more-than-k-nodes/?ref=rp
Given a tree with N node values from 1 to N and (N-1) Edges and a number K,
the task is to remove the minimum number of nodes from the tree such that
every subtree will have at most K nodes. Removing nodes will remove the edges,
from that nodes to all other connected nodes.
*/


/*
                  1
              /   \   \
             2    3    4
            /      \    \
           5       6     7
          / \       \
         8  9       10

*/

#include <iostream>
#include <vector>

using namespace std;


//We represent the tree as vector<vector<int>>--> adjacency list
//We perform dfs, we update the count

int dfs(vector <bool> visited, int key, vector<vector<int>> adj, int &K, int removed, vector <int> node_removed)
{
  //start is the starting node where we currently are now
  visited[key]=true;
  int node_count = 1;
  for (int child: adj[key])
  {
    if (visited[child])
      continue;

    //Perform the count of nodes. We use recusive call to count the number of nodes
    node_count+=dfs(visited,key,adj,K,removed,node_removed);
  }

  //if node_count > K start
  if (node_count > K)
  {
    //incremennt the removed
    removed++;
    //keep track of the nodes removed.
    node_removed.push_back(key);
    node_count = 0;
  }
  return node_count;
}


//Function remove nodes
void removeNodes(vector <bool> &visited, int K,int & removed,vector <int> node_removed, vector<vector<int>> &adj)
{
  //Call dfs here
  dfs(visited,1 ,adj,K,removed,node_removed);
  cout << "The number of nodes removed" << removed << endl;

  //The nodes removed are as follows

  for (int node : node_removed)
  {
    cout << "The identity of the nodes removed are: " << node << endl;
  }
}

//in place adding of the numbers in the form:
//(1,2) --> means 1 is connected to 2 here.
void addEdge(vector <vector<int>> &adj, int a, int b)
{
  //a is connected to b, b is also connected to a
  adj[a].push_back(b);
  adj[b].push_back(a);
}

int main()
{
  //Add tree edges from adjacency list --> Vector datatype
  //Then we run a DFS update the count each time
  //If the number of nodes > K in each subtree, then
  //we remove the nodes not needed and keep track of the count of nodes.

  //size of adjacency list here we take for instance N as 20 or any big number;
  int N = 20;

  //Given K
  int K = 3;

  //keep track of the nodes_count;
  int node_count = 0;

  vector <bool> visited(N);
  //Keep track of number of nodes removed
  int removed = 0;
  //keep track of  the number of count we call the

  //Keep track of the 'name' of the nodes removed;
  vector <int> node_removed;

  //Build the graph from the adjacency list here:
  vector <vector<int>> adj(N);

  //Call the function addEdge for edj,
  addEdge(adj,1,2);
  addEdge(adj,1,3);
  addEdge(adj,1,4);
  addEdge(adj,2,5);
  addEdge(adj,5,8);
  addEdge(adj,5,9);
  addEdge(adj,3,6);
  addEdge(adj,6,10);
  addEdge(adj,4,7);
  //removeNodes Function call
  removeNodes(visited, K, removed, node_removed, adj);
  return 0;
}


//TODO: Print the stuffs in main:
