import unittest

# O(N)
# Can also sort strings and then compare with each other O(NlogN)
def check_permutation(str1, str2):
    chars_count = {}

    for char in str1:
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1

    for char in str2:
        if char in chars_count:
            chars_count[char] -= 1
        else:
            return False

    diff_counts = set(chars_count.values())
    if len(diff_counts) <= 1 and 0 in diff_counts:
        return True
    else:
        return False

class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = check_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = check_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
