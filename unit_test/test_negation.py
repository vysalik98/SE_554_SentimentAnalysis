import unittest
from program.sentiment_analysis_functions import AntonymReplacer

class TestNegationHandling(unittest.TestCase):

    def func_to_test(self,string):
        func = AntonymReplacer().replace_neg(string=string)
        return func
    
    def test_neg_true(self):
       
        negation = self.func_to_test(string="this is not nice")
        self.assertEqual(negation.strip(), 'this is nasty', msg='Equal')
    
    
    def test_neg_not_true(self):
        
        negation = self.func_to_test(string='I am not good')
        self.assertNotEqual(negation, 'I am not good')


    def test_neg_is_not_none(self):
        
        negation = self.func_to_test(string='this is not fun')
        self.assertIsNotNone(negation)


    def test_neg_is_none(self):
        
        negation = self.func_to_test(string='')
        self.assertIsNone(None if (negation=='') else negation)


    def test_neg_type_error(self):
        
        negation = self.func_to_test(string='')
        self.assertRaises(TypeError, negation)
    


if __name__ == "__main__":
    unittest.main()