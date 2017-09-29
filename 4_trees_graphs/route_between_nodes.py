import unittest
from Graph import Graph, Node
from Queue import Queue


# Bidirection search version, O( (max # adjacent nodes) ^ (distance / 2)) time
# Nonbidirection just use BFS (first from one node, than other for directed graph)
def RBN(g, a, b):
    visitedA = set()
    visitedA.add(a)

    visitedB = set()
    visitedB.add(b)

    toVisitA = Queue()
    toVisitA.enqueue(a)

    toVisitB = Queue()
    toVisitB.enqueue(b)

    while True:
        for x in range(toVisitA.size()):
            current = toVisitA.dequeue()
            if current == b:
                return True
            for node in current.children:
                if node not in visitedA:
                    toVisitA.enqueue(node)

        for x in range(toVisitB.size()):
            current = toVisitB.dequeue()
            if current == a:
                return True
            for node in current.children:
                if node not in visitedB:
                    toVisitA.enqueue(node)

        # Directed graph, undirected use or
        if toVisitA.size() == 0 and toVisitB.size() == 0:
            return False


class Test(unittest.TestCase):
    # Directed graphs
    g = Graph()
    a = Node(1)
    b = Node(1)
    c = Node(1)
    a.children.append(b)
    b.children.append(a)

    g.children.append(a)
    g.children.append(b)
    g.children.append(c)

    def test(self):
        self.assertEqual(RBN(self.g, self.a, self.b), True)
        self.assertEqual(RBN(self.g, self.a, self.c), False)


if __name__ == "__main__":
    unittest.main()
