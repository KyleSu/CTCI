import unittest
from LinkedList import LinkedList


# SINGLE LINKED LIST
def return_kth_last(ll, k):
    if ll.head is None:
        return None

    current = ll.head
    runner = ll.head

    for i in range(k):
        runner = runner.next
        if runner is None:
            return None

    while runner is not None:
        current = current.next
        runner = runner.next

    return current


class Test(unittest.TestCase):
    list = LinkedList()
    list.add(4)
    list.add(10)
    list.add(5)
    list.add(6)

    def test_remove_dup(self):
        self.assertEqual(return_kth_last(self.list, 3).value, 10)
        self.assertTrue(return_kth_last(self.list, 5) is None)


if __name__ == "__main__":
    unittest.main()
