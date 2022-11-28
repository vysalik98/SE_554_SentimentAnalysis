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
        with open(test_file, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, dialect='excel')
            writer.writerows(rows)

    def tearDown(self):
        os.remove(test_file)

    def test_read_line(self):
        with open(test_file, 'r') as csv_file:
            reader = csv.reader(csv_file, dialect='excel')
            self.assertEqual(next(reader), rows[0])
            self.assertEqual(next(reader), rows[1])


if __name__ == "__main__":
    unittest.main()
