import unittest

# O(N)
# Can also be done by searching for each char in remainder of string
# No extra space but O(N^2) time
def is_unique(str):
    # Assuming character set is ASCII (128 characters)
    # ASK FOR CHARACTER SET
    if len(str) > 128:
        return False

    chars = {}
    for char in str:
        if char in chars:
            return False
        else:
            chars[char] = True
    return True

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = is_unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = is_unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
