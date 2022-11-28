import unittest
from program.sentiment_analysis_functions import AntonymReplacer

class TestReplace(unittest.TestCase):

    def func_to_test(self,string):
        func = AntonymReplacer().replace_word(string)
        return func

    def test_replace_true(self):
    
        replace = self.func_to_test(string="n't")
        self.assertEqual(replace, ' not', msg='Equal')

    def test_replace_not_true(self):
        
        replace = self.func_to_test(string="won't")
        self.assertNotEqual(replace, "won't")

    def test_replace_is_not_none(self):
        
        replace = self.func_to_test(string='good')
        self.assertIsNotNone(replace)

    def test_replace_type_error(self):
        
        replace = self.func_to_test(string='')
        self.assertRaises(TypeError, replace, [])


if __name__ == "__main__":
    unittest.main()