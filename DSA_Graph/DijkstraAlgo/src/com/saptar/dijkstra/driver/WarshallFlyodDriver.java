package com.saptar.dijkstra.driver;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

import com.saptar.bellmanford.engine.BellmanFord;
import com.saptar.dijkstra.model.*;
import com.saptar.warshallflyod.engine.WarshallFlyod;

public class WarshallFlyodDriver {
	 final static int INF = 99999, V = 4;

	public static void main (String[] args)
{
    /* Let us create the following weighted graph
       10
    (0)------->(3)
    |         /|\
    5 |          |
    |          | 1
    \|/         |
    (1)------->(2)
       3           */
    int graph[][] = { {0,   5,  INF, 10},
                      {INF, 0,   3, INF},
                      {INF, INF, 0,   1},
                      {INF, INF, INF, 0}
                    };
    WarshallFlyod a = new WarshallFlyod();

    // Print the solution
    a.flyodWarshal(graph);
}
}