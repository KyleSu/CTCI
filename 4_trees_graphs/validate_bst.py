import unittest
from Graph import BSTNode, Tree


# Given a binary tree, validate if it is a search tree
def validate(node, lo=None, hi=None):
    if node is None:
        return True

    if lo is None and hi is None:
        return validate(node.left, None, node.value) and validate(node.right, node.value, None)
    elif lo is None:
        if node.value > hi:
            return False

        return validate(node.left, None, node.value) and validate(node.right, node.value, hi)

    elif hi is None:
        if node.value < lo:
            return False

        return validate(node.left, lo, node.value) and validate(node.right, node.value, None)

    else:
        if node.value < lo or node.value > hi:
            return False

        return validate(node.left, lo, node.value) and validate(node.right, node.value, hi)


def validate_tree(tree):
    root = tree.root
    return validate(root)


class Test(unittest.TestCase):
    a = BSTNode(1)
    b = BSTNode(2)
    c = BSTNode(3)
    d = BSTNode(4)
    e = BSTNode(5)
    f = BSTNode(6)
    g = BSTNode(7)
    b.left = a
    b.right = c
    d.left = b
    f.left = e
    f.right = g
    d.right = f
    tree_valid = Tree(d)

    def test_valid(self):
        self.assertTrue(validate_tree(self.tree_valid))

    a = BSTNode(1)
    b = BSTNode(2)
    c = BSTNode(0)
    b.left = a
    b.right = c
    tree_invalid = Tree(b)

    def test_invalid(self):
        self.assertFalse(validate_tree(self.tree_invalid))


if __name__ == "__main__":
    unittest.main()
