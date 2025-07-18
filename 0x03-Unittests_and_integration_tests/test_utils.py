#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from utils import memoize

class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        """Test that memoize caches the result of a method."""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mock_method:
            test_obj = TestClass()
            # Call a_property twice
            result1 = test_obj.a_property()
            result2 = test_obj.a_property()

            # Check if result is correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Ensure a_method was only called once due to memoization
            mock_method.assert_called_once()
