import unittest


# O(N)
def urlify(string, length):
    for i in range(len(string)):
        if string[i] == ' ':
            for x in range(len(string) - 3, i, -1):
                string[x + 2] = string[x]
            string[i:i + 3] = '%20'

    return string


class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
