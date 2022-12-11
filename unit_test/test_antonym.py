#########################################################################################
# Author        Title
# ******        ****************
# Saurav        test Antonym
#   
# Purpose       : Unit Test Cases for testing antonym function  
# Environment   : Venv (Dependencies in requirements.txt)
#########################################################################################

import unittest
from sentiment_analysis_functions import SentimentAnalysis

  
class Test_Antonym(unittest.TestCase):
  
    def testNotNone(self):
        resp = SentimentAnalysis().get_antonym(word = "happy")     
        self.assertIsNotNone(resp)

    def testNotEqual(self):
        resp = SentimentAnalysis().get_antonym(word = "happy")     
        self.assertNotEqual(resp,"happy")

    def testNone(self):
        resp = SentimentAnalysis().get_antonym(word = "is")     
        self.assertIsNone(resp)

if __name__ == '__main__':
    unittest.main()