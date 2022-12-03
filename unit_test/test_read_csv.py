#########################################################################################
# Author        Title
# ******        ****************
# Prachi        test_read_csv
#   
# Purpose       : Unit Test Cases for the function readcsv    
# Environment   : Venv (Dependencies in requirements.txt)
# Usage         : python3 -m unit_test/test_read_csv.py
#########################################################################################

import os
import csv
import unittest

test_file = 'test.csv'
rows = [
    ['0a', '0b'],
    ['1a', '1b'],
]
class TestCsv(unittest.TestCase):

    def setUp(self):
        with open(test_file, 'w', newline='') as readcsv:
            writer = csv.writer(readcsv, dialect='excel')
            writer.writerows(rows)

    def tearDown(self):
        os.remove(test_file)

    def test_read_line(self):
        with open(test_file, 'r') as readcsv:
            reader = csv.reader(readcsv, dialect='excel')
            self.assertEqual(next(reader), rows[0])
            self.assertEqual(next(reader), rows[1])


if __name__ == "__main__":
    unittest.main()
