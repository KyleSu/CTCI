from LinkedList import LinkedList
import unittest

# Only given reference to node to be deleted
def delete_middle(n):
    n.value = n.next.value
    n.next = n.next.next

class Test(unittest.TestCase):
    list = LinkedList()
    list.add(4)
    list.add(10)
    middle = list.add(5)
    list.add(6)

    remove_list = LinkedList()
    remove_list.add(4)
    remove_list.add(10)
    remove_list.add(6)

    def test_remove_middle(self):
        delete_middle(self.middle)
        self.assertEqual(self.list, self.remove_list)


if __name__ == "__main__":
    unittest.main()
