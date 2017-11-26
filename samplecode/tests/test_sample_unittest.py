import unittest
import sample_unittest

class TestSample(unittest.TestCase):
    def test_add(self):
        self.assertEqual(sample_unittest.add(1,2), 3)
if __name__ == "__main__":
    unittest.main()