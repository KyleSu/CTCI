import unittest


class StackNode:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return str(self.value)


class Stack:

    def __init__(self):
        self.top = None

    def __iter__(self):
        current = self.top
        while current is not None:
            yield current
            current = current.next

    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def __eq__(self, other):
        return str(self) == str(other)

    def push(self, value):
        if (self.top is None):
            new_node = StackNode(value)
        else:
            new_node = StackNode(value, self.top)
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            return None
        else:
            top_value = self.top.value
            self.top = self.top.next
            return top_value

    def peek(self):
        return self.top.value

    def isEmpty(self):
        return self.top is None

    def size(self):
        count = 0
        current = self.top
        while current is not None:
            count += 1
            current = current.next
        return count


class Test(unittest.TestCase):
    stack1 = Stack()
    stack1.push(5)
    stack1.push(4)
    stack1.push(3)
    stack1.pop()

    stack2 = Stack()
    stack2.push(5)
    stack2.push(4)

    def test_stack(self):
        self.assertEqual(self.stack1, self.stack2)
        self.assertEqual(self.stack1.peek(), 4)


if __name__ == "__main__":
    unittest.main()
