import unittest
import coolify as cl

class test_coolify(unittest.TestCase):
    def test_coolify(self):
       name = "Chris"
       self.assertTrue(cl.coolify(name) == "Chris is cool")
       self.assertFalse(cl.coolify(name) == "Chris")


if __name__ == '__main__':
    unittest.main()
