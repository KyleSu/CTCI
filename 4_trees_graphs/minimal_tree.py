import unittest
from Graph import BSTNode, Tree


# Given a sorted array, form a minimal length binary tree
def minTree(array):
    root = createTree(array, 0, len(array) - 1)
    tree = Tree(root)
    return tree


def createTree(array, lo, hi):
    if lo == hi:
        leaf = BSTNode(array[lo])
        return leaf
    elif lo == hi - 1:
        node = BSTNode(array[hi])
        node.left = createTree(array, lo, lo)
        return node
    else:
        mid = lo + ((hi - lo) // 2)
        node = BSTNode(array[mid])
        node.left = createTree(array, lo, mid - 1)
        node.right = createTree(array, mid + 1, hi)
        return node


class Test(unittest.TestCase):
    root = BSTNode(3)
    a = BSTNode(0)
    b = BSTNode(1)
    c = BSTNode(2)
    b.left = a
    b.right = c
    root.left = b

    d = BSTNode(4)
    e = BSTNode(5)
    f = BSTNode(6)
    e.left = d
    e.right = f
    root.right = e

    tree = Tree(root)

    arr = [0, 1, 2, 3, 4, 5, 6]

    def test(self):
        self.assertEqual(self.tree, minTree(self.arr))


if __name__ == "__main__":
    unittest.main()
