# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time = O(1) Avg, Space = O(1)
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.dfs(root)
    
    def dfs(self, root: Optional[TreeNode]) -> None:
        while root != None:
            self.stack.append(root)
            root = root.left
        

    def next(self) -> int:
        popped = self.stack.pop()
        self.dfs(popped.right)
        return popped.val
        

    def hasNext(self) -> bool:
        return len(self.stack) >0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()