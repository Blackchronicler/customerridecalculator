import unittest
import datetime
from calculations import calc_costs


class MyTest(unittest.TestCase):

    def test_duration_hours_costs(self):
        start_date = "2022-06-28 16:44:26"
        start_date_time_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
        end_date = "2022-06-28 20:44:26"
        end_date_time_obj = datetime.datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')

        self.assertEqual(calc_costs(start_date_time_obj, end_date_time_obj)[0], 240)
        self.assertEqual(calc_costs(start_date_time_obj, end_date_time_obj)[1], 120.00)

    def test_duration_days_costs(self):
        start_date = "2022-06-25 16:44:26"
        start_date_time_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
        end_date = "2022-06-28 20:44:26"
        end_date_time_obj = datetime.datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')

        self.assertEqual(calc_costs(start_date_time_obj, end_date_time_obj)[0], 40)
        self.assertEqual(calc_costs(start_date_time_obj, end_date_time_obj)[1], 2280.00)

if __name__ == '__main__':
    unittest.main()