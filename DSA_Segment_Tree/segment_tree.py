class Node:
    def __init__(self, start,end):
        self.start = start
        self.end = end
        self.sum = 0
        self.lazy = 0
        self.right = None
        self.left = None

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.root = self.build(nums,0,len(nums)-1)
    def build(self,nums,start,end):
        node = Node(start,end)
        if start == end:
            node.sum = nums[start]
            return node
        mid = (start + end)//2
        node.left = self.build(nums,start,mid)
        node.right = self.build(nums,mid+1,end)
        node.sum = node.left.sum + node.right.sum
        return node
    
    def update(self, index, val):
        self.update_helper(self.root, index, val)
    
    def update_helper(self, root, index, val):
        if root.start == root.end:
            root.sum = val
            return
        
        M = (root.start + root.end) // 2
        if index > M:
            self.update_helper(root.right, index, val)
        else:
            self.update_helper(root.left, index, val)
        root.sum = root.left.sum + root.right.sum
    def query(self, L, R):
        return self.query_helper(self.root, L, R)

    def query_helper(self, root, L, R):
        if L <= root.start and root.end <= R:
            return root.sum
        
        if R < root.start or L > root.end:
            return 0
        
        return self.query_helper(root.left, L, R) + self.query_helper(root.right, L, R)
    

    
    
    

