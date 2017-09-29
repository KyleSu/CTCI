import StackModule as SM
import unittest


class QueueViaStack:
    def __init__(self):
        self.addStack = SM.Stack()
        self.removeStack = SM.Stack()

    def push(self, value):
        self.addStack.push(value)

    def pop(self):
        if self.removeStack.isEmpty():
            while not self.addStack.isEmpty():
                self.removeStack.push(self.addStack.pop())

        return self.removeStack.pop()


class Test(unittest.TestCase):
    a = QueueViaStack()
    a.push(1)
    a.push(2)

    def test_a(self):
        b = self.a.pop()
        c = self.a.pop()
        self.assertEqual(b, 1)
        self.assertEqual(c, 2)


if __name__ == "__main__":
    unittest.main()
