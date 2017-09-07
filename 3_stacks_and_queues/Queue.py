import unittest


class QueueNode:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node
        self.prev = None

    def __str__(self):
        return str(self.value)


class Queue:

    def __init__(self):
        self.top = None
        self.bottom = None

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

    def enqueue(self, value):
        if (self.top is None):
            new_node = QueueNode(value)
        else:
            new_node = QueueNode(value, self.top)
            self.top.prev = new_node
        self.top = new_node
        if self.isEmpty():
            self.bottom = self.top 

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            bottom_value = self.bottom.value
            if self.bottom == self.top:
                self.top = None
            self.bottom = self.bottom.prev
            self.bottom.next = None
            return bottom_value

    def peek(self):
        return self.bottom.value

    def isEmpty(self):
        return self.bottom is None


class Test(unittest.TestCase):
    queue1 = Queue()
    queue1.enqueue(5)
    queue1.enqueue(4)
    queue1.enqueue(3)

    queue2 = Queue()
    queue2.enqueue(4)
    queue2.enqueue(3)

    def test_queue(self):
        self.assertEqual(self.queue1, self.queue2)
        self.assertEqual(self.queue1.peek(), 4)


if __name__ == "__main__":
    unittest.main()
