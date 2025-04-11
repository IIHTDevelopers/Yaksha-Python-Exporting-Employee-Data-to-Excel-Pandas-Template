import unittest
from mainclass import EmployeeDataAnalysis
from test.TestUtils import TestUtils
import pandas as pd


class ExceptionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.analysis = EmployeeDataAnalysis("employee_data.csv")
        cls.test_obj = TestUtils()

    def test_invalid_csv_path(self):
        """Test handling of a non-existent CSV file."""
        try:
            EmployeeDataAnalysis("non_existent.csv")
            self.test_obj.yakshaAssert("TestInvalidCsvPath", False, "exceptional")
            print("TestInvalidCsvPath = Failed")
        except:
            self.test_obj.yakshaAssert("TestInvalidCsvPath", True, "exceptional")
            print("TestInvalidCsvPath = Passed")

    def test_invalid_column_access(self):
        """Test behavior when accessing a non-existent column."""
        try:
            self.analysis.df["Invalid_Column"]
            self.test_obj.yakshaAssert("TestInvalidColumnAccess", False, "exceptional")
            print("TestInvalidColumnAccess = Failed")
        except KeyError:
            self.test_obj.yakshaAssert("TestInvalidColumnAccess", True, "exceptional")
            print("TestInvalidColumnAccess = Passed")
        except:
            self.test_obj.yakshaAssert("TestInvalidColumnAccess", False, "exceptional")
            print("TestInvalidColumnAccess = Failed")
