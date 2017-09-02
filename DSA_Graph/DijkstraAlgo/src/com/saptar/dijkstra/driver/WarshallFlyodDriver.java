package com.saptar.dijkstra.driver;

import com.saptar.warshallflyod.engine.WarshallFlyod;

public class WarshallFlyodDriver {
	final static int INF = 99999, V = 4;

	public static void main(String[] args) {
		int graph[][] = { { 0, 5, INF, 10 }, { INF, 0, 3, INF },
				{ INF, INF, 0, 1 }, { INF, INF, INF, 0 } };
		WarshallFlyod a = new WarshallFlyod();

		// Print the solution
		a.flyodWarshal(graph);
	}
}
