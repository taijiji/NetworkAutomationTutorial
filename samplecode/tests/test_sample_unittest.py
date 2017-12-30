import unittest
import sample_unittest

class TestSample(unittest.TestCase):
    def test_add(self):
        expected    = 3
        actual      = sample_unittest.add(1,2)
        self.assertEqual(expected, actual)

        expected    = 3
        actual      = sample_unittest.add(2,2)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()