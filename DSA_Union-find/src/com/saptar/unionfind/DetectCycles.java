package com.saptar.unionfind;

public class DetectCycles {
	// find the subset to which element i belongs
	public int find(int parent[], int i){
		if(parent[i] == -1){
			return i;
		}
		return find(parent,parent[i]);
	}
	
	public void union(int parent[], int x, int y){
		int setX = this.find(parent, x);
		int setY = this.find(parent, y);
		parent[setX] = setY;
	}
	
	public int isCycle(Graph graph){
		// initialize subset corresponding to each vertex
		int parent[] = new int[graph.V];
		for(int idx = 0; idx < graph.V; idx++){
			parent[idx] = -1;
		}
		// iterate over each edge and figure out if 
		// src and dest of any edge falls under one subset
		for(int idx = 0; idx < graph.E; idx++){
			int x = this.find(parent,graph.edge[idx].src);
			int y = this.find(parent,graph.edge[idx].dest);
			if(x == y){
				return 1;
			}
			this.union(parent, x, y);
			
		}
		return 0;
	}

}
