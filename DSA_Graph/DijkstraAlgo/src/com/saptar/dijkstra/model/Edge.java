package com.saptar.dijkstra.model;

import com.saptar.dijkstra.model.Vertex;

public class Edge {
	private String id;
	private Vertex sourceVertex;
	private Vertex destinationVertex;
	private int weight;
	
	public Edge(String id, Vertex sourceVertex, Vertex destinationVertex, int weight){
		this.id = id;
		this.sourceVertex = sourceVertex;
		this.destinationVertex = destinationVertex;
		this.weight = weight;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Vertex getSourceVertex() {
		return sourceVertex;
	}

	public void setSourceVertex(Vertex sourceVertex) {
		this.sourceVertex = sourceVertex;
	}

	public Vertex getDestinationVertex() {
		return destinationVertex;
	}

	public void setDestinationVertex(Vertex destinationVertex) {
		this.destinationVertex = destinationVertex;
	}

	public int getWeight() {
		return weight;
	}

	public void setWeight(int weight) {
		this.weight = weight;
	}
	
	@Override
	public String toString(){
		return this.getSourceVertex()+" "+this.getDestinationVertex();
	}
}
