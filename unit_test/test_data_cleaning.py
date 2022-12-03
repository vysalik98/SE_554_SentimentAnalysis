#########################################################################################
# Author        Title
# ******        ****************
# Prachi        test_data_cleaning
#   
# Purpose       : Unit Test Cases for the function text_data_cleaning    
# Environment   : Venv (Dependencies in requirements.txt)
# Usage         : python3 -m unittest  -v unit_test/test_data_cleaning.py     
#########################################################################################

import unittest
from program.sentiment_analysis_functions import SentimentAnalysis

class TestDataCleaning(unittest.TestCase):

    def func_to_test(self,word):
        func = SentimentAnalysis().text_data_cleaning(sentence=sentence)

    def test_data_cleaning_true(self):
        """
        This function is meant to test if two values are equal
        :param: word
        :return: assertion result
        """
        cleanedSentence = self.func_to_test(sentence='Food is good,.')
        self.assertEqual(cleanedSentence, 'Food is good', msg='Equal')

    def test_data_cleaning_true(self):
        """
        This function is meant to check the inequality of two values 
        :param: word
        :return: assertion result
        """
        cleanedSentence = self.func_to_test(sentence='Food is good,.')
        self.assertNotEqual(cleanedSentence, 'Food is good,.')

    def test_data_cleaning_is_none(self):
        """
        This function is meant to check that input value is None or not
        :param: word
        :return: assertion result
        """
        cleanedSentence = self.func_to_test(sentence='Food is good')
        self.assertIsNone(cleanedSentence)


    def test_data_cleaning_is_not_none(self):
        """
        This function is meant to check that input value is None or not
        :param: word
        :return: assertion result
        """
        cleanedSentence = self.func_to_test(sentence='Food is good')
        self.assertIsNotNone(cleanedSentence)

    def test_data_cleaning_type_error(self):
        """
        This function is meant to verify that a specific exception gets raised
        :param: word
        :return: assertion result
        """
        cleanedSentence = self.func_to_test(sentence='')
        self.assertRaises(TypeError, cleanedSentence, [])


if __name__ == "__main__":
    unittest.main()
