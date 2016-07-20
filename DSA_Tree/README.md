### Tree Data Structure

Tree represents nodes connected by edges. We are going to learn binary tree or binary search tree specifically.  
Binary tree is a special data structure used for storage purposes. A binary tree has special condition in that, each node can have two children at maximum. A binary tree have benifits of both an ordered array and linked list as search is as quick as a sorted array and insertion or deletion is as fast as a linked list.  

#### Terminologies
Following are important terms with respect to a tree:  
- Path - Refers to sequence of nodes along the edges.  
- Root - Node at the top of the tree is called root. There is only one root per tree and one path from root node to any node.  
- Parent - Any node except root node has one path upward to a node called parent node of that node.  
- Child - Node below a given node connected path a path from the given node downwards is called the child node of that node.  
- Leaf - Node which does not have any child node is called as a leaf node of the tree.  
- Subtree - Subtree represents decendant of a node.  
- Visiting - Refers to checking value of a node when the control is on that node.  
- Traversing - Traversing means passing through a node in a specific order.  
- Levels - Level of a node represents the generation of the node.  
- Keys - Key represent a value of a node based on which a search operation is to be carried out.  

#### Binary Search Tree (BST) representation.  
Binary search tree represnts a special behaviour. The node's left child must have value less than that of the node and the right node must have value greater than that of the node. A tree node must have a structure as follows:  
```sh
struct node{
	int data;
	struct node* rightChild;
	struct node* leftChild;
}
```
All tree node shares common structure.

#### BST basic operations

The basic operation that can be performed on a binary tree data structure:  
- Insert - insert an element in a tree/ create a tree.  
- Search - search an element in a tree.  
- pre-order traversal - traverse a tree in a pre-ordered manner.  
- post-order traversal - traverse a tree in 
