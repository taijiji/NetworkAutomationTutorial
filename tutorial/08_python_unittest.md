# Unittest

Original script

```python
def add(x, y):
    return x + y
```

test script

mkdir tests
touch tests/test_sample_unittest.py

```python
import unittest
import sample_unittest

class TestSample(unittest.TestCase):
    def test_add(self):
        self.assertEqual(sample_unittest.add(1,2), 3)
if __name__ == "__main__":
    unittest.main()
```

```
python3 -m unittest tests.test_sample_unittest


.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```