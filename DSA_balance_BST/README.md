## Balanced Binary Search Tree.

A balanced Binary tree or a self balancing binary search tree is said to be one where the difference of height between the left subtree and the right subtree is not more than **1**.  
This difference is know as the **balance factor**.

### Why have a self balancing BST?

What if the input to the binary search tree comes in a sorted manner?  
In such a case, we would end up having a left subtree heavy(in case the input is decending) or a right subtree heavy(in case the input in ascending) binary search tree. In such a case the worst case time complexity would be somewhere in the vivinity of lineary search, which is O(n). In order to have an efficient search on a BST, it is obvious that the worst time complexity should be managed somewhere in the vicinity of O(logn). To achieve this, we need algorithms which self balances a BST, at times when a simple insertion or deletion would render the tree unbalanced.

### Types of self balancing tree

There are two common types of self balancing tree:  
1. AVL tree - This is a self balancing tree, which ensure that the balance factor of 1 is maintained after every deletion or insertion.  
2. Red Black Tree - This is another type of balancing tree where individual nodes can have two colors, red and black. It also confirms to certain rules(discussed later).  

An AVL tree as compared to a red black tree is more balance, but every insertion or deletion involves costly manipulations. So choose AVL tree when the primary objective is to cater to search on the data and chose red black, when there is a considerable amount of data insertion/deletion.  

### AVL Tree

As mentioned above AVL tree is a self balancing tree. For more detailed analysis of AVL tree pls checkout [nptel IITD](https://www.youtube.com/watch?v=TbvhGcf6UJU) lecture on you tube.  

#### AVL tree insertion

To make sure that the given tree remains AVL after every insertion, we mush augment the standard BST insertion insertion operation to perform .  
Following are the two basic operations that can be performed to re-balance a bst without violation the BST property.  
```sh
T1, T2 and T3 are subtrees of the tree rooted with y (on left side) 
or x (on right side)           
                y                               x
               / \     Right Rotation          /  \
              x   T3   – – – – – – – >        T1   y 
             / \       < - - - - - - -            / \
            T1  T2     Left Rotation            T2  T3
Keys in both of the above trees follow the following order 
      keys(T1) < key(x) < keys(T2) < key(y) < keys(T3)
So BST property is not violated anywhere.

```

Steps to follow for insertion:  
Let the newly inserted node be w  
1. Perform standard BST insert for w.  
2. Start from the newly inserted node w and travel up and first unbalanced node . Let Z be the first unbalanced node, y be the child of z that comes on the path from w to z and x be the grandchild of z that comes in the path from w to z.  
3. Re-balance the tree by performing appropriate rotations on the subtree rooted with z. There can be 4 possible casses that needs to be handled as x,y and z can be arranged in 4 ways. Following are the possible 4 arrangements.   
- y is left child of z and x is left child of y (left left case)  
- y is left child of z and x is right child of y (left right case)  
- y is right child of z and x is right child of y (right right case)  
- y is right child of z and x is left child of y(right left case)  
Following are the operations that needs to be performed in the above mentioned cases. In all cases , we need to re-balance the subtree rooted with z and the complete tree becoms balanced as the height of the subtree rooted with z becomes same as it was before insertion.   

- Left Left Case:  
 	```sh
 		T1, T2, T3 and T4 are subtrees.
	         z                                      y 
	        / \                                   /   \
	       y   T4      Right Rotate (z)          x      z
	      / \          - - - - - - - - ->      /  \    /  \ 
	     x   T3                               T1  T2  T3  T4
	    / \
	  T1   T2	
 	```
- Left Right Case  
 	```sh
 	     z                               z                           x
	    / \                            /   \                        /  \ 
	   y   T4  Left Rotate (y)        x    T4  Right Rotate(z)    y      z
	  / \      - - - - - - - - ->    /  \      - - - - - - - ->  / \    / \
	T1   x                          y    T3                    T1  T2 T3  T4
	    / \                        / \
	  T2   T3                    T1   T2
 	```
And so on for the other two cases.  

Implementation:  
The implementation presented here uses recursive BST insert to insert a new node. In the recursive BST insert after insertion we get pointers to all ancestors one by one in bottom up manner. So we don't need parent pointer to travel up. The recursive code itself travels up and visits all the ancestors of the newly inserted node.  




