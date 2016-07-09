## Stack Data structure

Stack is an abstract data type (ADT) , commonly used in programming languages.  
Stack DS , just like , any real world stack allows operations at one end only.  
At any given time we can access the top element of the stack.  
As such this is an example of LIFO Data Structure.

### Basic operations on stack

- push() - pushing/storing element on the stack
- pop() - removing or accessing element from the stack.  

To use a stack efficiently , we need to check the status of the status and for the same reason the following  
functionality has been added as well  

- peek() - to get the top element with out actually removing it.
- isFull() - check if stack is full and
- isEmpty() - check if the stack is empty.  

At all times we maintain a pointer to the last pushed data in the stack, which represents the 'TOP' of the stack.