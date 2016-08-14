package com.saptar.dijkstra.driver;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

import com.saptar.bellmanford.engine.BellmanFord;
import com.saptar.dijkstra.model.*;

public class BellmanFordAlgorithmDriver {
	static List<Vertex> nodes;
	static List<Edge> edges;
	public static void main(String[] args) {

		nodes = new ArrayList<Vertex>();
		edges = new ArrayList<Edge>();
		for(int i=0; i< 7 ; i ++){
			nodes.add(new Vertex("Node "+i, "Node "+i));
		}
	    addLane("Edge_0", 0, 1, 10);
	    addLane("Edge_1", 0, 2, -80);
	    addLane("Edge_3", 1, 2, 6);
	    addLane("Edge_4", 2, 3, 70);
	    addLane("Edge_5", 1, 4, -20);
	    addLane("Edge_6", 4, 5, 50);
	    addLane("Edge_7", 4, 6, -10);
	    addLane("Edge_8", 6, 5, 5);
	    // test for negative cycle
	    //addLane("Edge_9", 2, 0, -20);
	    
	    Graph graph = new Graph(nodes, edges);
	    BellmanFord algo = new BellmanFord(graph);
	    algo.execute(nodes.get(0));
	    LinkedList<Vertex> path = new LinkedList<Vertex>();
	    path = algo.getPath(nodes.get(3));
	    System.out.println(Arrays.toString(path.toArray()));


	}

	private static void addLane(String laneId, int sourceLocNo, int destLocNo,
			int duration) {
		Edge lane = new Edge(laneId, nodes.get(sourceLocNo),
				nodes.get(destLocNo), duration);
		edges.add(lane);
	}

}
