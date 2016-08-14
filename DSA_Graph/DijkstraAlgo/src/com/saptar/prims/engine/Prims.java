package com.saptar.prims.engine;


public class Prims {
	private static final int V=5;
	// a utility function to find the vertex with
	// minimum key value which is not included in the mst.
	public int minKey(int key[], Boolean mstSet[]){
		int min = Integer.MAX_VALUE;
		int min_index = -1;
		for(int idx = 0; idx<V; idx++){
			if(mstSet[idx]== false && key[idx] < min){
				min = key[idx];
				min_index = idx;
			}
		}
		return min_index;
	}
	// A utility function to print the constructed MST stored in
    // parent[]
    public void printMST(int parent[], int n, int graph[][])
    {
        System.out.println("Edge   Weight");
        for (int i = 1; i < V; i++)
            System.out.println(parent[i]+" - "+ i+"    "+
                               graph[i][parent[i]]);
    }
   
    public void primsMST(int graph[][]){
    	// hold the info on parent 
    	// the index represents the second node 
    	// and the actual value represents the first node.
    	// so parent[3] = 2 means the parent node for 3 is 2.
    	int parent[] = new int[V];
    	// array to hold the key value for all the vertices
    	int key[] = new int[V];
    	// set to represent if a vertice has been already absorbed into the
    	// mst
    	Boolean mstSet[] = new Boolean[V];
    	// initialize all keys as infinite
    	for(int idx = 0; idx < V; idx++){
    		key[idx] = Integer.MAX_VALUE;
    		mstSet[idx] = false; 
    	}
    	// first node is always choose
    	key[0] = 0;
    	parent[0] = -1;
    	// iterate for n-1 time
    	for(int idx = 0; idx < V-1; idx++){
    		int u = minKey(key, mstSet);
    		mstSet[u] = true;
    		// check this node's adjacent node and set its values
    		for(int count = 0; count<V; count++){
    			if(graph[u][count]!=0 && mstSet[count] == false 
    					&& graph[u][count] < key[count]){
    				parent[count] = u; // parent of count would be u
    				key[count] = graph[u][count];
    			}
    		}
    	}
    	printMST(parent, V, graph);
    }
}
