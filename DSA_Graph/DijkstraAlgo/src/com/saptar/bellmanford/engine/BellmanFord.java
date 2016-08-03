package com.saptar.bellmanford.engine;

import com.saptar.dijkstra.model.*;

import java.util.List;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Map;

public class BellmanFord {
	final private List<Vertex> vertices;
	final private List<Edge> edges;
	private Map<Vertex, Vertex> predecessors;
	private Map<Vertex, Integer> distance;
	
	public BellmanFord(Graph graph){
		vertices = new ArrayList<Vertex>(graph.getVertices());
		edges = new ArrayList<Edge>(graph.getEdges());
	}
	public void execute(Vertex source){
		// initiate distance and predecessor
		distance = new HashMap<Vertex, Integer>();
		predecessors = new HashMap<Vertex, Vertex>();
		// step 1: set distances to all other vertex except
		// source to infinity
		for(Vertex node: vertices){
			if(!(node.equals(source))){
				distance.put(node, Integer.MAX_VALUE);
			}
		}
		// set the source vertex distance to 0
		distance.put(source, 0);
		// step 2 : iterate # vertices - 1 times
		// first iteration guarantees shortes paths
		// which are atmost one edge long.
		// second iteration, two edges long and so on.
		for(int i = 0; i < vertices.size(); i++){
			// iterate over all the node
			for(int j=0; j< edges.size(); j++){
				Vertex sourceNode = edges.get(j).getSourceVertex();
				Vertex destinationNode = edges.get(j).getDestinationVertex();
				if(distance.get(sourceNode)+ edges.get(j).getWeight() < distance.get(destinationNode)){
					distance.put(destinationNode, (distance.get(sourceNode)+ edges.get(j).getWeight()));
					// change predecessor
					predecessors.put(destinationNode, sourceNode);
				}
			}
		}
		// step 3: detect negative cycle
		// if there is a negative cycle then
		// sourcedistance + weight of edge to destination < destination
		for(int j=0; j< edges.size(); j++){
			Vertex sourceNode = edges.get(j).getSourceVertex();
			Vertex destinationNode = edges.get(j).getDestinationVertex();
			if(distance.get(sourceNode)+ edges.get(j).getWeight() < distance.get(destinationNode)){
				System.out.println("Negative cycles detcted");
				System.exit(0);
			}
		}

	}
	// get the path
	public LinkedList<Vertex> getPath(Vertex destination){
		LinkedList<Vertex> path = new LinkedList<Vertex>();
		Vertex targetNode = destination;
		path.add(destination);
		if(predecessors.get(destination) == null){
			return null;
		}
		while(predecessors.get(targetNode) != null){
			targetNode = predecessors.get(targetNode);
			path.add(targetNode);
		}
		return path;
	}
}
