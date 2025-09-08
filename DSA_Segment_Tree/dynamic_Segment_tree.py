'''
implementation details:
This segment tree uses a node-based structure to dynamically create only the parts of the tree that are needed, allowing handling very large index ranges without allocating large arrays upfront.

Lazy propagation is used to delay updates to child nodes until necessary, improving efficiency for range updates.


'''

class Node:
    def __init__(self):
        self.left = None   # left child
        self.right = None  # right child
        self.sum = 0       # sum of the segment
        self.lazy = 0      # lazy propagation value

class DynamicSegmentTree:
    def __init__(self, start, end):
        self.root = Node()
        self.start = start  # overall range start
        self.end = end      # overall range end

    def _push_down(self, node, start, end):
        """Push lazy updates to children."""
        if node.lazy != 0:
            mid = (start + end) // 2
            # Create children if not exist
            if node.left is None:
                node.left = Node()
            if node.right is None:
                node.right = Node()

            # Propagate lazy value to children
            node.left.sum += (mid - start + 1) * node.lazy
            node.left.lazy += node.lazy

            node.right.sum += (end - mid) * node.lazy
            node.right.lazy += node.lazy

            # Clear lazy value at current node
            node.lazy = 0

    def _update_range(self, node, start, end, l, r, val):
        if node is None or r < start or l > end:
            return
        if l <= start and end <= r:
            node.sum += (end - start + 1) * val
            node.lazy += val
            return

        self._push_down(node, start, end)
        mid = (start + end) // 2

        if node.left is None:
            node.left = Node()
        if node.right is None:
            node.right = Node()

        self._update_range(node.left, start, mid, l, r, val)
        self._update_range(node.right, mid + 1, end, l, r, val)

        node.sum = (node.left.sum if node.left else 0) + (node.right.sum if node.right else 0)

    def update_range(self, l, r, val):
        """Add val to all elements in index range [l, r]."""
        if l > r or r < self.start or l > self.end:
            return
        l = max(l, self.start)
        r = min(r, self.end)
        self._update_range(self.root, self.start, self.end, l, r, val)

    def _query_range(self, node, start, end, l, r):
        if node is None or r < start or l > end:
            return 0
        if l <= start and end <= r:
            return node.sum

        self._push_down(node, start, end)
        mid = (start + end) // 2
        left_sum = self._query_range(node.left, start, mid, l, r)
        right_sum = self._query_range(node.right, mid + 1, end, l, r)
        return left_sum + right_sum

    def query_range(self, l, r):
        """Return sum of elements in index range [l, r]."""
        if l > r or r < self.start or l > self.end:
            return 0
        l = max(l, self.start)
        r = min(r, self.end)
        return self._query_range(self.root, self.start, self.end, l, r)
