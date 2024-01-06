from datetime import datetime
import unittest

from parsers.sofi_cc import parse as sofi_parse
from parsers.tests.sofi_cc_html import sofi_test_data

class TestSofiCC(unittest.TestCase):
    def test_parse(self):
        parsed = list(sofi_parse(sofi_test_data))

        expect = [
            [datetime(2024, 1, 5), 'Market32 pchopper #250', 'Groceries', '58.56', 0],
            [datetime(2024, 1, 4), 'Aldi 65228', 'Groceries', '100.70', 0],
            [datetime(2024, 1, 4), 'Shopjimmycom', 'Shopping', '27.66', 0],
            [datetime(2024, 1, 4), 'Thrive market', 'Other', '64.15', 0],
            [datetime(2024, 1, 3), 'Thrive market', 'Other', '19.16', 0],
            [datetime(2024, 1, 2), 'Auto-pay thank you', 'Payment', 0, '5478.67'],
            [datetime(2023, 12, 31), 'Aldi 65183', 'Groceries', '53.58', 0],
            [datetime(2023, 12, 31), 'Via dino discovery', 'Entertainment', '21.60', 0],
            [datetime(2023, 12, 30), 'Ulta.com', 'Shopping', '97.20', 0],
            [datetime(2023, 12, 29), 'Aldi.us', 'Groceries', '137.80', 0],
            [datetime(2023, 12, 28), 'Market32 pchopper #250', 'Groceries', '46.18', 0],
            [datetime(2023, 12, 27), 'Stewarts shop 365', 'Groceries', '7.51', 0],
            [datetime(2023, 12, 26), 'Sq *rochester ice cent', 'Other', '10.00', 0],
            [datetime(2023, 12, 23), 'Market32 pchopper #250', 'Groceries', '27.20', 0],
            [datetime(2023, 12, 23), 'Hannaford #8267', 'Groceries', '25.04', 0],
            [datetime(2023, 12, 22), 'Stewarts shop 365', 'Groceries', '27.52', 0],
            [datetime(2023, 12, 20), 'Stewarts shop 365', 'Groceries', '5.99', 0],
            [datetime(2023, 12, 20), 'Sp theplanthatch', 'Shopping', '80.25', 0],
            [datetime(2023, 12, 20), 'Walmart.com', 'Shopping', '2.43', 0],
            [datetime(2023, 12, 20), 'Sq *olivia sutcliffe', 'Fitness & Self Care', '20.00', 0],
            [datetime(2023, 12, 19), 'Walmart.com', 'Shopping', '46.93', 0],
            [datetime(2023, 12, 19), 'Walmart.com', 'Shopping', '5.51', 0],
            [datetime(2023, 12, 18), 'Target.com *', 'Shopping', '4.99', 0],
            [datetime(2023, 12, 18), 'Aldi.us', 'Groceries', '110.39', 0],
            [datetime(2023, 12, 18), 'Michaels #9490', 'Shopping', '5.23', 0],
            [datetime(2023, 12, 17), 'Trader joe s #574', 'Groceries', '6.78', 0],
            [datetime(2023, 12, 17), 'Walmart.com', 'Shopping', '52.43', 0],
            [datetime(2023, 12, 17), 'Halfmoon petroleum i', 'Transportation', '36.03', 0],
            [datetime(2023, 12, 16), 'Party city bopis', 'Shopping', '12.20', 0],
            [datetime(2023, 12, 15), 'Netflix.com', 'Bills & Utilities', '16.57', 0],
            [datetime(2023, 12, 15), 'Market32 pchopper #250', 'Groceries', '25.30', 0],
            [datetime(2023, 12, 15), 'Walmart.com', 'Shopping', '95.33', 0],
            [datetime(2023, 12, 14), 'Market32 pchopper #112', 'Groceries', '116.30', 0],
            [datetime(2023, 12, 14), 'Asha 3', 'Gifts & Donations', '253.00', 0],
            [datetime(2023, 12, 12), 'Stewarts shop 365', 'Groceries', '7.80', 0],
            [datetime(2023, 12, 12), 'Aldi 65228', 'Groceries', '7.29', 0],
            [datetime(2023, 12, 12), 'Lowes #01740*', 'Home', 0, '207.30'],
            [datetime(2023, 12, 12), 'Lowes #01740*', 'Home', 0, '81.07'],
            [datetime(2023, 12, 12), 'Lowes #01740*', 'Home', '112.97', 0],
            [datetime(2023, 12, 12), 'Lowes #01740*', 'Home', '355.21', 0],
            [datetime(2023, 12, 12), 'Target 00014779', 'Groceries', '6.26', 0],
            [datetime(2023, 12, 12), 'Target 00014779', 'Groceries', '70.40', 0],
            [datetime(2023, 12, 11), 'Cvs/pharmacy #02072', 'Medical', '2.75', 0],
            [datetime(2023, 12, 11), 'Market32 pchopper #038', 'Groceries', '44.48', 0],
            [datetime(2023, 12, 11), 'Michaels #9490', 'Shopping', '3.74', 0],
            [datetime(2023, 12, 11), 'Michaels stores 2029', 'Shopping', '32.22', 0],
            [datetime(2023, 12, 11), 'Target 00014779', 'Groceries', '38.61', 0],
            [datetime(2023, 12, 10), 'Usps po 3500580215', 'Other', '39.60', 0],
            [datetime(2023, 12, 10), 'Joann stores #1929', 'Shopping', '42.16', 0],
            [datetime(2023, 12, 9), 'Lowes #00907*', 'Home', '27.03', 0],
            [datetime(2023, 12, 9), 'Lowes #00907*', 'Home', '54.04', 0],
            [datetime(2023, 12, 8), 'Stewarts shop 365', 'Groceries', '13.80', 0],
            [datetime(2023, 12, 8), 'Tst* ala shanghai', 'Dining & Drinks', '44.04', 0],
            [datetime(2023, 12, 7), 'Aldi 65183', 'Groceries', '7.83', 0]
        ]

        self.assertEqual(len(expect), len(parsed))
        for i, expected in enumerate(expect):
            self.assertEqual(expected, parsed[i])
