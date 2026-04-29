# class TreeNode:
#   def __init__(self,val = 0, left = None, right = None):
#       this.val = val
#       this.left = None
#.      this.right= None

class Solution:
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root