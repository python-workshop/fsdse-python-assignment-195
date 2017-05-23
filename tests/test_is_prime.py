from unittest import TestCase


class TestIs_prime(TestCase):
    def test_is_prime(self):
        try:
            from build import is_prime
        except ImportError:
            self.assertFalse("no function found")

        self.assertEqual(False, is_prime(0))
        self.assertEqual(False, is_prime(1))

        self.assertEqual(True, is_prime(2))
        self.assertEqual(True, is_prime(3))
        self.assertEqual(True, is_prime(7))
        self.assertEqual(True, is_prime(5))
        self.assertEqual(True, is_prime(11))
        self.assertEqual(True, is_prime(13))
        self.assertEqual(True, is_prime(17))
        self.assertEqual(True, is_prime(19))
        self.assertEqual(True, is_prime(199))
        self.assertEqual(True, is_prime(197))