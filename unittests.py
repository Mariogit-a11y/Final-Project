import unittest

from data_set import DataSet
from city import City
from employment_data import EmploymentData

class Test(unittest.TestCase):
    def test_categorize_education(self):
        c = City("Cali", "CA")
        high = EmploymentData(c, 2020, 5.0, 50.0)
        med1 = EmploymentData(c, 2020, 5.0, 35.0)
        med2 = EmploymentData(c, 2020, 5.0, 49.99)
        low = EmploymentData(c, 2020, 5.0, 34.99)

        self.assertEqual(high.categorize_education(), "High")
        self.assertEqual(med1.categorize_education(), "Medium")
        self.assertEqual(med2.categorize_education(), "Medium")
        self.assertEqual(low.categorize_education(), "Low")


    def test_display_summary(self):
        c = City("Austin", "TX")
        e = EmploymentData(c, 2021, 4.25, 52.5)
        summary = e.display_summary()

        self.assertIn("City:Austin, TX", summary)
        self.assertIn("Year:2021", summary)
        self.assertIn("Unemployment rate:4.25%", summary)
        self.assertIn("Education level (Bachelors and Graduate):52.5%", summary)
        self.assertIn("Education category:High", summary)


class TestDataSet(unittest.TestCase):
    def setUp(self):
        self.data_set = DataSet()
        self.data_set.records = [
            EmploymentData(City("A", "TA"), 2020, 7.0, 40.0),   # medium
            EmploymentData(City("B", "TB"), 2020, 3.0, 55.0),   # high
            EmploymentData(City("C", "TC"), 2020, 10.0, 30.0),  # low
        ]


    def test_calculate_averages(self):
        averages = self.data_set.calculate_averages()

        self.assertEqual(averages["average_unemployment"], 6.67)
        self.assertEqual(averages["average_education"], 41.67)
        self.assertIn("overall_averages", self.data_set.results)


    def test_find_highest_and_lowest(self):
        highest = self.data_set.find_highest()
        lowest = self.data_set.find_lowest()

        self.assertEqual(highest.unemployment_rate, 10.0)
        self.assertEqual(highest.city, City("C", "TC"))

        self.assertEqual(lowest.unemployment_rate, 3.0)
        self.assertEqual(lowest.city, City("B", "TB"))

        self.assertIn("highest_unemployment", self.data_set.results)
        self.assertIn("lowest_unemployment", self.data_set.results)


    def test_group_by_education(self):
        groups = self.data_set.group_by_education()

        self.assertEqual(len(groups["High"]), 1)
        self.assertEqual(len(groups["Medium"]), 1)
        self.assertEqual(len(groups["Low"]), 1)

        self.assertEqual(groups["High"][0].city, City("B", "TB"))
        self.assertEqual(groups["Medium"][0].city, City("A", "TA"))
        self.assertEqual(groups["Low"][0].city, City("C", "TC"))


    def test_sort_records(self):
        self.data_set.sort_records("unemployment", True)
        self.assertEqual([r.unemployment_rate for r in self.data_set.records], [10.0, 7.0, 3.0])

        self.data_set.sort_records("education", False)
        self.assertEqual([r.education_level for r in self.data_set.records], [30.0, 40.0, 55.0])

if __name__ == '__main__':
    unittest.main()