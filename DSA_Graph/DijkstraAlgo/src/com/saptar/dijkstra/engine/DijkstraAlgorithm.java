package com.saptar.dijkstra.engine;

import java.util.List;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Map;
import java.util.Set;
import java.util.HashSet;
import java.util.Collections;

import javax.management.RuntimeErrorException;

import com.saptar.dijkstra.model.Vertex;
import com.saptar.dijkstra.model.Edge;
import com.saptar.dijkstra.model.Graph;

public class DijkstraAlgorithm {
	private final List<Vertex> nodes;
	private final List<Edge> edges;
	private Set<Vertex> settledNodes;
	private Set<Vertex> unSettledNodes;
	private Map<Vertex, Vertex> predecessors;
	private Map<Vertex, Integer> distance;
	
	public DijkstraAlgorithm(Graph graph){
		this.nodes = new ArrayList<Vertex>(graph.getVertices());
		this.edges = new ArrayList<Edge>(graph.getEdges());
	}
	
	public void execute(Vertex source){
		settledNodes = new HashSet<Vertex>();
		unSettledNodes = new HashSet<Vertex>();
		distance = new HashMap<Vertex, Integer>();
		predecessors = new HashMap<Vertex, Vertex>();
		distance.put(source, 0);
		unSettledNodes.add(source);
		while(unSettledNodes.size() > 0){
			Vertex node = getMinimum(unSettledNodes);
			settledNodes.add(node);
			unSettledNodes.remove(node);
			findMinimalDistance(node);
		}
	}
	private void findMinimalDistance(Vertex node) {
		List<Vertex> adjacentNode = getNeighbour(node);
		for(Vertex vertex : adjacentNode){
			if(getShortestDistance(vertex) > getShortestDistance(node)+ getDistance(node , vertex)){
				distance.put(vertex, getShortestDistance(node)+ getDistance(node , vertex));
				predecessors.put(vertex, node);
				unSettledNodes.add(vertex);
			}
		}
		
	}

	private int getDistance(Vertex node, Vertex vertex) {
		for(Edge edge: edges){
			if(edge.getSourceVertex().equals(node) && edge.getDestinationVertex().equals(vertex)){
				return edge.getWeight();
			}
		}
		throw new RuntimeErrorException(null, "should not happen");
	}

	private List<Vertex> getNeighbour(Vertex node) {
		List<Vertex> neighbours = new ArrayList<Vertex>();
		for(Edge edge: edges){
			if(edge.getSourceVertex().equals(node) && !isSettled(edge.getDestinationVertex())){
				neighbours.add(edge.getDestinationVertex());
			}
		}
		return neighbours;
	}

	private boolean isSettled(Vertex destinationVertex) {
		return settledNodes.contains(destinationVertex);
	}

	/**
	 * get the minimum 
	 */
	private Vertex getMinimum(Set<Vertex> vertices){
		Vertex minimum = null;
		for(Vertex vertex: vertices){
			if(minimum == null){
				minimum = vertex;
			}
			else{
				if(getShortestDistance(vertex)< getShortestDistance(minimum)){
					minimum = vertex;
				}
			}
		}
		return minimum;
	}

	private int getShortestDistance(Vertex vertex) {
		Integer d = distance.get(vertex);
		if(d == null){
			return Integer.MAX_VALUE;
		}
		else{
			return d;
		}
	}
	public LinkedList<Vertex> getPath(Vertex target){
		LinkedList<Vertex> path = new LinkedList<Vertex>();
		Vertex step = target;
		if(predecessors.get(step) == null){
			return null;
		}
		path.add(step);
		while(predecessors.get(step) != null){
			step = predecessors.get(step);
			path.add(step);
		}
		// put it in order
		Collections.reverse(path);
		return path;
	}
}


