class Node:
    def __init__(self, data, color="red", left=None, right=None, parent=None):
        self.data = data
        self.color = color  # Nodes are either 'red' or 'black'
        self.left = left
        self.right = right
        self.parent = parent


class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0, color="black")  # Sentinel node to represent null
        self.root = self.TNULL

    def insert(self, key):
        # Create a new node to be inserted
        new_node = Node(key)
        new_node.left = self.TNULL
        new_node.right = self.TNULL
        
        # Perform a normal BST insertion
        parent = None
        current = self.root
        
        while current != self.TNULL:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right
        
        new_node.parent = parent
        
        if parent is None:
            self.root = new_node  # Tree was empty, new node becomes root
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        # If the new node is the root node, make it black
        if new_node.parent is None:
            new_node.color = "black"
            return
        
        # If the grandparent is None, don't fix anything
        if new_node.parent.parent is None:
            return
        
        # Fix violations of red-black tree properties
        self.fix_insert(new_node)

    # for re-color the node
    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fix_insert(self, k):
        while k.parent.color == "red":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # Uncle
                if u.color == "red":
                    # Case 1: Uncle is red, recolor and move up the tree
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        # Case 2: Rotate to the right
                        k = k.parent
                        self.rotate_right(k)
                    # Case 3: Rotate to the left
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.rotate_left(k.parent.parent)
            else:
                u = k.parent.parent.right  # Uncle
                if u.color == "red":
                    # Case 1: Uncle is red, recolor and move up the tree
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        # Case 2: Rotate to the left
                        k = k.parent
                        self.rotate_left(k)
                    # Case 3: Rotate to the right
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.rotate_right(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "black"

    # Visualization helper to print the tree structure as text
    def visualize(self, node, indent="", last=True):
        if node != self.TNULL:
            print(indent, end="")
            if last:
                print("R----", end="")
                indent += "     "
            else:
                print("L----", end="")
                indent += "|    "
            
            color = "Red" if node.color == "red" else "Black"
            print(f"{node.data} ({color})")
            self.visualize(node.left, indent, False)
            self.visualize(node.right, indent, True)

    # Wrapper function to start visualization from root
    # Recursive function to visualize the tree structure
    def print_tree(self):
        self.visualize(self.root)

    # Helper function for in-order traversal
    def __inorder_helper(self, node):
        if node != self.TNULL:
            self.__inorder_helper(node.left)
            print(f"{node.data} ({node.color})", end=" ")
            self.__inorder_helper(node.right)

    # Print in-order traversal of the tree
    def inorder(self):
        self.__inorder_helper(self.root)
        print()


# Example usage:

rbt = RedBlackTree()
rbt.insert(47)
rbt.insert(23)
rbt.insert(71)
rbt.insert(14)
rbt.insert(35)
rbt.insert(59)
rbt.insert(87)
rbt.insert(8)
rbt.insert(76)

# Now insert 5 and 17 as per the question
rbt.insert(5)
rbt.insert(17)

# Print in-order traversal to check node arrangement
print("In-order Traversal:")
rbt.inorder()

# Print the tree structure in text format
print("\nTree Structure Visualization:")
rbt.print_tree()