/*

#Cold Blooded Writing of BFS search

import collections

#DFS Algorithm
def BFS(graph, root):
    visited = set()
    queue   = collections.deque([root])
    visited.add(root)

    while queue:
        #Dequque a vertex from Queue
        vertex = queue.popleft()
        print (str(vertex) + " ", end=" ")

        #if not visited, mark as visited and
        #enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                #for set we use add, for list we use append
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == "__main__":
    graph = {0:[1,2], 1:[2],2:[3],3:[1,2]}
    print ('Following is Breadth First Traversal:')
    BFS(graph,0)

*/

//Question: *A means the value at the memmory location where the pointer is
//poiinting to. '&' in c++ means the address of the variable it is attached
//to. so here. &*A=> &(*A)=> A. ie, It takes the address of the content of
//the memmory location where the pointer is pointing to..which means the
//pointer value itself.


//TODO: Function to build the graph, function to add adjacency List

#include <iostream>
#include <list>

using namespace std;

class Graph
{
  int numVertices;
  list<int>* adjLists;
  bool* visited;

   public:
  Graph(int vertices);
  void addEdge(int src, int dest);
  void BFS(int startVertex);
};

// Create a graph with given vertices,
// and maintain an adjacency list
Graph::Graph(int vertices) {
  numVertices = vertices;
  adjLists = new list<int>[vertices];
}

// Add edges to the graph
void Graph::addEdge(int src, int dest) {
  adjLists[src].push_back(dest);
  adjLists[dest].push_back(src);
}

// BFS algorithm
void Graph::BFS(int startVertex)
{
  visited = new bool[numVertices];
  for (int i = 0; i < numVertices; i++)
    visited[i] = false;

  list<int> queue;

  visited[startVertex] = true;
  queue.push_back(startVertex);

  list<int>::iterator i;

  while (!queue.empty())
  {
    int currVertex = queue.front();
    cout << "Visited " << currVertex << " ";
    queue.pop_front();

    for (i = adjLists[currVertex].begin(); i != adjLists[currVertex].end(); ++i)
    {
      int adjVertex = *i;
      if (!visited[adjVertex])
      {
        visited[adjVertex] = true;
        queue.push_back(adjVertex);
      }
    }
  }
}

int main() {
  Graph g(4);
  g.addEdge(0, 1);
  g.addEdge(0, 2);
  g.addEdge(1, 2);
  g.addEdge(2, 0);
  g.addEdge(2, 3);
  g.addEdge(3, 3);

  g.BFS(2);

  return 0;
}
