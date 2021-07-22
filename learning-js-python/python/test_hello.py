import unittest
from hello import hello

class Testing(unittest.TestCase):

    def test_hello(self):
        result = hello()
        self.assertEqual(result, "Hello")

if __name__ == '__main__':
    unittest.main()

# def test_hello():
#     assert hello() == 'Hello', "Should be Hello"
#
# if __name__ == "__main__":
#     test_hello()
#     print("Everything passed")
