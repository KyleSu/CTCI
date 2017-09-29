import unittest
from Graph import BSTNode


# Given a BST node, find the next succesor in the tree (Node can access parent)
# Throw error if none possible

def find_next(node):
    if node.right is not None:
        next = node.right
        while next.left is not None:
            next = next.left

        return next
    else:
        # Catch case where given root, no right children
        if node.parent is None:
            return None
        if node == node.parent.left:
            return node.parent
        else:
            prev = node
            # Go up tree until node is left child
            while prev != prev.parent.left:
                # Catch root
                if prev.parent is None:
                    return None
                prev = prev.parent
            return prev.parent


class Test(unittest.TestCase):
    a = BSTNode(1)
    b = BSTNode(2)
    c = BSTNode(3)
    d = BSTNode(4)
    e = BSTNode(5)

    b.left = a
    a.parent = b
    b.right = c
    c.parent = b
    d.left = b
    b.parent = d
    d.right = e
    e.parent = d

    def test(self):
        self.assertEqual(find_next(self.a), self.b)
        self.assertEqual(find_next(self.c), self.d)
        self.assertEqual(find_next(self.d), self.e)


if __name__ == "__main__":
    unittest.main()
