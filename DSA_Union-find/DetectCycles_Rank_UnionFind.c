#include <stdio.h>
#include <stdlib.h>

struct Edge{
	int src;
	int dest;
};

struct Graph{
	int V;
	int E;
	struct Edge* edge;
};

struct Subset{
	int parent;
	int rank;
};

struct Graph* createGraph(int noVertex, int noEdge){
	struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));
	graph -> V = noVertex;
	graph -> E = noEdge;
	// array of edges
	graph -> edge = (struct Edge*) malloc(graph -> E * sizeof(struct Edge));
	return graph;
}

// utility function to find the subset of element i from array of subsets
// use path compression optimization technique.
int find(struct Subset subsets[], int i){
	if(subsets[i].parent != i){
		// path compression by assingin the root of the tree
		// which the element i is a part of to the 
		// parent of i
		subsets[i].parent = find(subsets, subsets[i].parent);
	}
	return subsets[i].parent;
}

void Union(struct Subset subsets[], int x, int y){
	int setX = find(subsets,x);
	int setY = find(subsets,y);

	if(subsets[setX].rank > subsets[setY].rank){
		subsets[setY].parent = setX;
	}
	else if(subsets[setX].rank < subsets[setY].rank){
		subsets[setX].parent = setY;
	}
	else{
		subsets[setY].parent = setX;
		subsets[setX].rank++;
	}
}

int isCycle(struct Graph* graph){
	int V = graph -> V;
	int E = graph -> E;

	// allocate mem for creating V sets
	struct Subset* subsets = (struct Subset*)malloc(V * sizeof(struct Subset));
	// initialise all the subset to contain one element and rank of 0
	for(int i = 0; i < V; i++){
		subsets[i].parent = i;
		subsets[i].rank = 0;
	}

	// iterate through all the edges of the graph and find the susbset for
	// vertices of each edge, if the subset of vertices for one edge comes
	// out to be equal , we have cycle in the graph
	// else do union.
	for(int j = 0; j<E; j++){
		int x = find(subsets,graph -> edge[j].src);
		int y = find(subsets,graph -> edge[j].dest);

		if(x == y){
			return 1;
		}
		else{
			Union(subsets,x,y);
		}
	}
}

// driver program
int main(){
	int V = 3;
	int E = 3;

	struct Graph* graph = createGraph(V,E);
	graph ->edge[0].src = 0;
	graph ->edge[0].dest = 1;

	graph ->edge[1].src = 1;
	graph ->edge[1].dest = 2;

	graph ->edge[2].src = 0;
	graph ->edge[2].dest = 2;

	int value = isCycle(graph);
	if(value == 1){
		printf("Cycle detected in the graph");
	}
	else{
		printf("Graph is acyclic");
	}
}