### Graph Data structure

A graph is a pictoral representation of a set of objects where some pairs of objects are connected by links.  
The interconnected objects are represented by points termed as vertices.  
Formally graph is a pair of sets (V, E) where  
V is set of vertices and  
E is the set of edges connecting some or all of the vertices.  

#### General terminlogies

We can represent a graph using an array of vertices and a two dimensional array of edges. Some important terms related to graphs are  
- *Vertex* : Each node of graph is represented as vertex.  
- *Edge* : Edge represents a path between two vertices .  
- *Adjacency* : Two nodes/vertices of a graph are said to be adjacent if they are connected through an edge.  
- *Path* : Path represents the sequence of edges between two vertices.  

#### Basic operations on a graph

- Add vertex  
- Add Egde  
- Display Vertex.  
- Traversing the graph.  

#### Depth First Search (DFS)

DFS travesrses the graph in depthward motion and uses the stack to remember to get to the next vertex when a dead end occurs in any iteration.  

Following are the basic rules for DFS  
- Rule 1 : Vist the adjacent unvisited vertex. Mark it as visited , display if necessary and push it to the stack.  
- Rule 2 : If no adjacent vertex found pop out the vertex from stack.  
- Rule 3 : Repeat rule 1 and 2 untill the stack is empty.

#### Breadh First Search (BFS)

BFS traverses the graph in breathwards motion and uses a queue to remember to get to the next vertex to start a search when dead end occurs in any iteration.  
Following are the basic rules for BFS  
- Rule 1 : Visit adjacent unvisited vertex. Mark it visited . Display it . Insert it in a queue.  
- Rule 2 : If no adjacent vertex found , remove the first vertex from queue.  
- Rule 3 : Repeat rule 1 an 2 untill the queue is empty.  