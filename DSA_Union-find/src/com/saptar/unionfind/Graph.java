package com.saptar.unionfind;

public class Graph {
	int V, E;
	Edge edge[];
	class Edge{
		int src, dest;
	}
	public Graph(int v, int e){
		this.V =v;
		this.E =e;
		edge = new Edge[this.E];
		for(int count = 0; count < this.E; count++){
			edge[count] = new Edge();
		}
	}
}
