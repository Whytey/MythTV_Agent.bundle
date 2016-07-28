__author__ = 'djwhyte'

import unittest


class MyTestCase(unittest.TestCase):

    def test_oldFile(self):
        self.assertEqual(True, False)


    def test_newFile(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
