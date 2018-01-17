# Unittest

Original script

```python
def add(x, y):
    sum = x + y
    return sum
```

directory
```
├── sample_unittest.py
└── tests
    └── test_sample_unittest.py
```

```python
import unittest
import sample_unittest

class TestSample(unittest.TestCase):
    def test_add(self):
        expected    = 3
        actual      = sample_unittest.add(1,2)
        self.assertEqual(expected, actual)

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

in case of failure

```
python3 -m unittest tests.test_sample_unittest
F
======================================================================
FAIL: test_add (tests.test_sample_unittest.TestSample)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/taiji/work/NetworkAutomationTutorial/samplecode/tests/test_sample_unittest.py", line 12, in test_add
    self.assertEqual(expected, actual)
AssertionError: 3 != 4

----------------------------------------------------------------------
Ran 1 test in 0.000s
````