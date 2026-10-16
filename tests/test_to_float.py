import unittest
import myclass.Weather as W
import myclass.Weather_circle as C
import myclass.Weather_forecast as F


class ToFloatTest(unittest.TestCase):
    def test_int_converti(self):
        for m in (W, C, F):
            self.assertEqual(m.to_float(0), 0.0)
            self.assertIsInstance(m.to_float(3), float)

    def test_bool_refuse(self):
        for m in (W, C, F):
            with self.assertRaises(AssertionError):
                m.to_float(True)


if __name__ == "__main__":
    unittest.main()
