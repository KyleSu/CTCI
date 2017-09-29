import unittest
from Graph import Node, Tree
from Queue import Queue
from copy import copy


# Return a list of lists, where each sublist contains all nodes at a certain depth
def list_depth(tree):
    root = tree.root

    next_level = Queue()
    current_level = Queue()
    current_level.enqueue(root)

    depthLists = []

    while not (next_level.isEmpty() and current_level.isEmpty()):
        if current_level.isEmpty():
            current_level = copy(next_level)
            next_level = Queue()

        depthLevel = []
        while not current_level.isEmpty():
            current_node = current_level.dequeue()
            depthLevel.append(current_node)
            for child in current_node.children:
                next_level.enqueue(child)

        depthLists.append(depthLevel)

    return depthLists


class Test(unittest.TestCase):
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)

    b.children.append(a)
    b.children.append(c)
    d.children.append(b)
    e.children.append(f)
    d.children.append(e)

    tree = Tree(d)

    expected = [[d], [b, e], [a, c, f]]

    def test(self):
        self.assertEqual(list_depth(self.tree), self.expected)


if __name__ == "__main__":
    unittest.main()

