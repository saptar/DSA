package com.saptar.unionfind;

public class DetectCyclesDriver {
	public static void main(String args[]){
		Graph graph = new Graph(3, 3);
		DetectCycles engine = new DetectCycles();
		 // add edge 0-1
        graph.edge[0].src = 0;
        graph.edge[0].dest = 1;
 
        // add edge 1-2
        graph.edge[1].src = 1;
        graph.edge[1].dest = 2;
 
        // add edge 0-2
        graph.edge[2].src = 0;
        graph.edge[2].dest = 2;
 
        if (engine.isCycle(graph)==1)
            System.out.println( "graph contains cycle" );
        else
            System.out.println( "graph doesn't contain cycle" );
	}

}
