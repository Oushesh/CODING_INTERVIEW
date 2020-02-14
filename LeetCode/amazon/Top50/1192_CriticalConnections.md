##  
  Intro:
    There are n servers numbered from 0 to n-1 connected by undirected
    server-server connections forming a network where connections[i] = [a,b]
    represents a connection between servers a & b. Any server can reach can
    reach any other server directly or indirectly through the network.

    A critical connection is a connection that, if removed, will make some server
    unable to reach some other server. connection[i] = [a,b] is removed.

    Return all critical connections in the network in any order.
