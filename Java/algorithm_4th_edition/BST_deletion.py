
# BST node defintion
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Algorithm
# 1. find the deleted node
# 2. if the node has no children, delete it
# 3. if the node has one child, replace it with the child
# 4. if the node has two children, replace it with the left successor

class Solution:
    def deleteNode(self, root, key: int):
        if not root:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            # store root.left
            root.left = self.deleteNode(root.left, key)
        # found the node
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Find the min from right subtree
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            # updating right node
            root.right = self.deleteNode(root.right, cur.val)

        return root
