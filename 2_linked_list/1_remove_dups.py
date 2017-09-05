import unittest
from LinkedList import LinkedList


# SINGLE LINKED LIST
def remove_dups(ll):
    if ll.head is None:
        return None

    current = ll.head
    seen = {current.value}

    while current.next is not None:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next

    return ll


# Follow up, no extra set allowed
def remove_dups_2(ll):
    if ll.head is None:
        return None

    current = ll.head

    while current is not None:
        runner = current
        while runner.next is not None:
            if current.value == runner.next.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return ll


class Test(unittest.TestCase):
    dups_list = LinkedList()
    dups_list.add(4)
    dups_list.add(10)
    dups_list.add(5)
    dups_list.add(5)
    dups_list.add(4)
    dups_list.add(6)
    dups_list.add(10)

    single_list = LinkedList()
    single_list.add(4)
    single_list.add(10)
    single_list.add(5)
    single_list.add(6)

    def test_remove_dup(self):
        self.assertEqual(remove_dups(self.dups_list), self.single_list)
        self.assertEqual(remove_dups_2(self.dups_list), self.single_list)


if __name__ == "__main__":
    unittest.main()
