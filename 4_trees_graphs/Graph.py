class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __eq__(self, other):
        if self.value != other.value:
            return False
        if len(self.children) != len(other.children):
            return False
        else:
            child_eq = True
            for x in range(len(self.children)):
                child_eq = child_eq and (self.children[x] == other.children[x])
            return child_eq


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __eq__(self, other):
        if self.value != other.value:
            return False
        else:
            if self.parent is None or other.parent is None:
                return self.parent == other.parent
            else:
                return self.parent.value == other.parent.value and self.left == other.left and self.right == other.right


class Tree:
    def __init__(self, root):
        self.root = root

    def __eq__(self, other):
        return self.root == other.root


class Graph:
    def __init__(self):
        self.children = []
