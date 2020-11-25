//COding INterview Test Code
//Blunt Trial to write DFS in Cpp given the notion in .py

#include <iostream>
#include <list>

/*
1. Build the graph
2. Build the adjacency Matrix in .cpp -> Different from python
   Python use dict and set better than list
3. Loop and add elements in the adjacency list. C++ sucks
4.
*/

using namespace std;

class Graph
{
  int numVertices;
  list <int> *adjLists;
  bool *visited;

  public:
    Graph(int V);
    void addEdge(int src, int dest);
    void DFS(int vertex);
};


//Initialize the Graph --> Constructor
Graph::Graph(int vertices)
{
  numVertices = vertices;
  adjLists = new list <int> [vertices];
  visited = new bool[vertices];
}

//add edges, take in adjacency List
void Graph::addEdge(int src, int dest)
{
  //Building a Graph
  adjLists[src].push_front(dest);
}

//DFS algorithm
void Graph::DFS(int vertex)
{
  //keep track of the visited indices
  visited[vertex] = true;
  //add neightbours to List
  list <int> adjList = adjLists[vertex];
  cout << vertex << " ";

  //STL Libraries list iterators:
  list <int>::iterator i;
  for (i=adjList.begin(); i!= adjList.end();++i)
  {
    if (!visited[*i])
    {
      DFS(*i);
    }
  }

}

int main()
{
  //Call Graph with number of vertices;
  Graph g(4);

  //Iteratively fill the elements
  g.addEdge(0,1);
  g.addEdge(0,2);
  g.addEdge(1,2);
  g.addEdge(2,3);

  g.DFS(0);
  return 0;
}
