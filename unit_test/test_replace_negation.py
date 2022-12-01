#########################################################################################
# Author        Title
# ******        **********************
# Vysali        test_replace_negation
#   
# Purpose       : Unit Test Cases for the function replace_neg    
# Environment   : Venv (Dependencies in requirements.txt)
# Usage         : python3 -m unittest  -v unit_test/test_replace_negation.py   
#########################################################################################

import logging
import unittest
from program.sentiment_analysis_functions import SentimentAnalysis

class TestNegationHandling(unittest.TestCase):

    def func_to_test(self,string):
        func = SentimentAnalysis().replace_neg(string=string)
        logging.info("Result through function : " + str(func))
        return func

    logging.info("Begin running test cases")
    
    def test_neg_true(self):
        """
        This function is meant to test if two values are equal
        :param: word
        :return: assertion result
        """
        negation = self.func_to_test(string='this is not good')
        self.assertEqual(negation.strip(), 'this is evil', msg='Equal')
    
    
    def test_neg_not_true(self):
        """
        This function is meant to check the inequality of two values 
        :param: word
        :return: assertion result
        """
        negation = self.func_to_test(string='I am not happy')
        self.assertNotEqual(negation, 'I am not happy')


    def test_neg_is_not_none(self):
        """
        This function is meant to check that input value is None or not
        :param: word
        :return: assertion result
        """
        negation = self.func_to_test(string='this is not fresh')
        self.assertIsNotNone(negation)


    def test_neg_is_none(self):
        """
        This function is meant to check that input value is None or not
        :param: word
        :return: assertion result
        """
        negation = self.func_to_test(string='')
        self.assertIsNone(None if (negation=='') else negation)


    def test_neg_type_error(self):
        """
        This function is meant to verify that a specific exception gets raised
        :param: word
        :return: assertion result
        """
        negation = self.func_to_test(string='')
        self.assertRaises(TypeError, negation)
    


if __name__ == "__main__":
    unittest.main()