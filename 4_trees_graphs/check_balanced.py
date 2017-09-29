import unittest
from Graph import BSTNode, Tree


# Given binary tree, check if balanced (height of two subtrees don't differ by more than 1)
def get_depth(node):
    if node is None:
        return 0

    max_depth = max(get_depth(node.left), get_depth(node.right))
    return max_depth + 1


def check_balance(node):
    if node.left is None and node.right is None:
        return True
    elif node.right is None:
        child = node.left
        child_depth = get_depth(child)

        return not child_depth > 1
    elif node.left is None:
        child = node.right
        child_depth = get_depth(child)

        return not child_depth > 1
    else:
        left_child = node.left
        right_child = node.right
        left_depth = get_depth(left_child)
        right_depth = get_depth(right_child)

        if abs(left_depth - right_depth) > 1:
            return False
        else:
            return check_balance(left_child) and check_balance(right_child)


class Test(unittest.TestCase):
    a = BSTNode(1)
    b = BSTNode(2)
    c = BSTNode(3)
    d = BSTNode(4)
    e = BSTNode(5)
    f = BSTNode(6)
    b.left = a
    b.right = c
    d.left = b
    e.right = f
    d.right = e
    tree1 = Tree(d)

    z = BSTNode(1)
    y = BSTNode(2)
    x = BSTNode(3)
    y.left = z
    x.left = y
    tree2 = Tree(x)

    def test(self):
        self.assertTrue(check_balance(self.tree1.root))
        self.assertFalse(check_balance(self.tree2.root))


if __name__ == "__main__":
    unittest.main()
