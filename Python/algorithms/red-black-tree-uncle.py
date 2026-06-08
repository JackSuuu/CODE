class Node:
    def __init__(self, data):
        self.data = data
        self.color = "RED"  # New nodes are always red
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = "BLACK"
        self.root = self.TNULL

    def left_rotate(self, x):
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

    def right_rotate(self, x):
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
        while k.parent and k.parent.color == "RED":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # Uncle
                if u and u.color == "RED":  # Case 1: Uncle is red
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:  # Case 2: Triangle
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = "BLACK"  # Case 3: Line
                    k.parent.parent.color = "RED"
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # Uncle
                if u and u.color == "RED":  # Case 1: Uncle is red
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:  # Case 2: Triangle
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = "BLACK"  # Case 3: Line
                    k.parent.parent.color = "RED"
                    self.right_rotate(k.parent.parent)
        self.root.color = "BLACK"

    def insert(self, key):
        node = Node(key)
        node.left = self.TNULL
        node.right = self.TNULL
        parent = None
        current = self.root

        while current != self.TNULL:
            parent = current
            if node.data < current.data:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.data < parent.data:
            parent.left = node
        else:
            parent.right = node

        if node.parent is None:
            node.color = "BLACK"
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)

    def inorder_helper(self, node):
        if node != self.TNULL:
            self.inorder_helper(node.left)
            print(f"{node.data} ({node.color})", end=" ")
            self.inorder_helper(node.right)

    def inorder(self):
        self.inorder_helper(self.root)
        print()

    def print_tree(self):
        def print_level(nodes, level, spacing):
            if not any(nodes):
                return
            next_level = []
            line = ""
            connectors = ""
            for i, node in enumerate(nodes):
                if node:
                    line += f"{node.data}({node.color[0]})".center(spacing)
                    next_level.append(node.left)
                    next_level.append(node.right)
                    if i % 2 == 0:
                        connectors += "/".center(spacing)
                    else:
                        connectors += "\\".center(spacing)
                else:
                    line += " ".center(spacing)
                    next_level.append(None)
                    next_level.append(None)
                    connectors += " ".center(spacing // 2)
            print(f"Level {level}: {line}")
            # if any(next_level):
            #     print(" " * (spacing // 5) + connectors)
            print_level(next_level, level + 1, spacing // 2)

        print_level([self.root], 0, 64)

# Example usage
if __name__ == "__main__":
    rbt = RedBlackTree()
    elements = [20, 15, 25, 10, 5, 1]
    for el in elements:
        rbt.insert(el)

    print("Inorder traversal of the Red-Black Tree:")
    rbt.inorder()

    print("\nTree structure:")
    rbt.print_tree()