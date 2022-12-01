#########################################################################################
# Author        Title
# ******        ****************
# Vysali        test_get_antonym
#   
# Purpose       : Unit Test Cases for the function get_antonym    
# Environment   : Venv (Dependencies in requirements.txt)
# Usage         : python3 -m unittest  -v unit_test/test_get_antonym.py     
#########################################################################################

import logging
import unittest
from program.sentiment_analysis_functions import SentimentAnalysis

class TestNegationHandling(unittest.TestCase):

    def func_to_test(self,word):
        func = SentimentAnalysis().get_antonym(word=word)
        logging.info("Result through function : " + str(func))
        return func

    logging.info("Begin running test cases")

    def test_antonym_true(self):
        """
        This function is meant to test if two values are equal
        :param: word
        :return: assertion result
        """
        antonym = self.func_to_test(word='good')
        self.assertEqual(antonym, 'evil', msg='Equal')

    def test_antonym_not_true(self):
        """
        This function is meant to check the inequality of two values 
        :param: word
        :return: assertion result
        """
        antonym = self.func_to_test(word='happy')
        self.assertNotEqual(antonym, 'happy')

    def test_antonym_is_none(self):
        """
        This function is meant to check that input value is None or not
        :param: word
        :return: assertion result
        """
        antonym = self.func_to_test(word='eat')
        self.assertIsNone(antonym)


    def test_antonym_is_not_none(self):
        """
        This function is meant to check that input value is None or not
        :param: word
        :return: assertion result
        """
        antonym = self.func_to_test(word='beautiful')
        self.assertIsNotNone(antonym)

    def test_antonym_type_error(self):
        """
        This function is meant to verify that a specific exception gets raised
        :param: word
        :return: assertion result
        """
        antonym = self.func_to_test(word='')
        self.assertRaises(TypeError, antonym, [])


if __name__ == "__main__":
    unittest.main()