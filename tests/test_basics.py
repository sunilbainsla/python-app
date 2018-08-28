import unittest
import sapient.basics as bas
class KnownValues(unittest.TestCase):
    def test_my_function(self):
        result =bas.my_function("SunilKumar")
        expected="SunilKumar Refsnes"
        self.assertEqual(expected,result)
        
if __name__=='__main__':
    unittest.main()
        
        