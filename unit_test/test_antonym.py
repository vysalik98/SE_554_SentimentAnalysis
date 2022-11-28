import unittest
from program.sentiment_analysis_functions import AntonymReplacer

class TestAntonym(unittest.TestCase):

    def func_to_test(self,word):
        func = AntonymReplacer().get_antonym(word=word)
        return func

    def test_antonym_true(self):
    
        antonym = self.func_to_test(word='nice')
        self.assertEqual(antonym, 'nasty', msg='Equal')

    def test_antonym_not_true(self):
        
        antonym = self.func_to_test(word='awesome')
        self.assertNotEqual(antonym, 'awesome')

    def test_antonym_is_none(self):
        
        antonym = self.func_to_test(word='average')
        self.assertIsNone(antonym)


    def test_antonym_is_not_none(self):
        
        antonym = self.func_to_test(word='good')
        self.assertIsNotNone(antonym)

    def test_antonym_type_error(self):
        
        antonym = self.func_to_test(word='')
        self.assertRaises(TypeError, antonym, [])


if __name__ == "__main__":
    unittest.main()