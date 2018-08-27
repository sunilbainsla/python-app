import unittest
import basics
class KnownValues(unittest.TestCase):
    def test_my_function(self):
        result =basics.my_function("SunilKumar")
        expected="SunilKumar Refsnes"
        self.assertEqual(expected,result)
        
if __name__=='__main__':
    unittest.main()
        
        