package com.saptar.kruskal.engine;

import java.util.*;


public class Graph {
	// A class to represent a graph edge
	class Edge implements Comparable<Edge>{
		int src, dest, weight;

		public int compareTo(Edge arg0) {
			return this.weight - arg0.weight;
		}
		
	};
	// A class to represent subset for union-find
	class Subset{
		int parent, rank;
	}
	
	int V,E; //V,E -> number of vertices and edges respectively.
	Edge edge[]; // collection of all edges
	
	// Creates a graph with V vertices and E edges
	public Graph(int v, int e){
		V = v;
		E = e;
		edge = new Edge[E];
		for(int i = 0; i < E; i++){
			edge[i] = new Edge();
		}
	}
	// An utility function to find the subset of an element
	// Uses path compression technique
	int find(Subset subsets[], int element){
		if(subsets[element].parent!= element){
			subsets[element].parent = find(subsets, subsets[element].parent);
		}
		return subsets[element].parent;
	}
	// An utility function that does union of
	// subsets of element X and Y
	void union(Subset subsets[], int x, int y){
		int rootX = find(subsets, x);
		int rootY = find(subsets, y);
		
		// if the rank of rootx is more than rooty
		// make rootx the parent of rooty
		if(subsets[rootX].rank > subsets[rootY].rank){
			subsets[rootY].parent = rootX;
		}
		else if(subsets[rootY].rank > subsets[rootX].rank){
			subsets[rootX].parent = rootY;
		}
		else{
			// if the rank is same
			subsets[rootY].parent = rootX;
			subsets[rootX].rank++;
		}
	}
	// the main function to construct MST using Kruskal's algorithm
	void KruskalMST(){
		Edge result[] = new Edge[V]; // This will store the result of the MST
		int e = 0;
		int i = 0;
		// number of edges in a MST can be vertices - 1
		for(i = 0; i < V ; i++){
			result[i] = new Edge();
		}
		// step 1 
		// sort the edges in ascending order
		Arrays.sort(edge);
		// step 2
		// select edges and figure out if its is forming a cycle
		// if not add it to result
		Subset  subsets[] = new Subset[V];
		for(i = 0; i < V ; i ++){
			// each vertex at the beginning form its own subset
			subsets[i] = new Subset();
		}
		for(int v = 0; v < V; v++){
			subsets[v].parent = v;
			subsets[v].rank = 0;
		}
		i = 0;
		while(e < V-1){
			Edge next_edge = new Edge();
			next_edge = edge[i++];
			
			int x = find(subsets, next_edge.src);
			int y = find(subsets, next_edge.dest);
			if(x!=y){
				result[e++] = next_edge;
				union(subsets, x, y);
			}		
		}
		System.out.println("Following are the edges in the constructed MST");
        for (i = 0; i < e; ++i)
            System.out.println(result[i].src+" -- "+result[i].dest+" == "+
                               result[i].weight);
	}
	
	// Driver program
	
	public static void main (String[] args)
    {
 
        /* Let us create following weighted graph
                 10
            0--------1
            |  \     |
           6|   5\   |15
            |      \ |
            2--------3
                4       */
        int V = 4;  // Number of vertices in graph
        int E = 5;  // Number of edges in graph
        Graph graph = new Graph(V, E);
 
        // add edge 0-1
        graph.edge[0].src = 0;
        graph.edge[0].dest = 1;
        graph.edge[0].weight = 10;
 
        // add edge 0-2
        graph.edge[1].src = 0;
        graph.edge[1].dest = 2;
        graph.edge[1].weight = 6;
 
        // add edge 0-3
        graph.edge[2].src = 0;
        graph.edge[2].dest = 3;
        graph.edge[2].weight = 5;
 
        // add edge 1-3
        graph.edge[3].src = 1;
        graph.edge[3].dest = 3;
        graph.edge[3].weight = 15;
 
        // add edge 2-3
        graph.edge[4].src = 2;
        graph.edge[4].dest = 3;
        graph.edge[4].weight = 4;
 
        graph.KruskalMST();
    }
}

