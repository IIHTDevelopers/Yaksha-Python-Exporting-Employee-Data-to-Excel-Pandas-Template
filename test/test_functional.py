import unittest
import pandas as pd
from mainclass import EmployeeDataAnalysis
from test.TestUtils import TestUtils
import os

class FunctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.analysis = EmployeeDataAnalysis("employee_data.csv")
        cls.test_obj = TestUtils()

    def test_csv_loading(self):
        """Test if the CSV file is loaded correctly."""
        try:
            if not self.analysis:
                self.test_obj.yakshaAssert("TestCSVLoading", False, "functional")
                print("TestCSVLoading = Failed")
                return
            obj = not self.analysis.df.empty
            self.test_obj.yakshaAssert("TestCSVLoading", obj, "functional")
            print("TestCSVLoading = Passed" if obj else "TestCSVLoading = Failed")
        except:
            self.test_obj.yakshaAssert("TestCSVLoading", False, "functional")
            print("TestCSVLoading = Failed")

    def test_display_head(self):
        """Test if the first 5 rows are returned correctly."""
        try:
            head = self.analysis.display_head()
            obj = len(head) == 5
            self.test_obj.yakshaAssert("TestDisplayHead", obj, "functional")
            print("TestDisplayHead = Passed" if obj else "TestDisplayHead = Failed")
        except Exception as e:
            print("TestDisplayHead = Failed")

    def test_highest_age_employee(self):
        """Check if the employee with highest age is identified correctly."""
        try:
            obj = self.analysis.highest_age_employee() == 104  # Assuming employee ID 104 is the oldest
            self.test_obj.yakshaAssert("TestHighestAgeEmployee", obj, "functional")
            print("TestHighestAgeEmployee = Passed" if obj else "TestHighestAgeEmployee = Failed")
        except:
            self.test_obj.yakshaAssert("TestHighestAgeEmployee", False, "functional")
            print("TestHighestAgeEmployee = Failed")

    def test_export_to_excel(self):
        """Check if the data is saved to an Excel file correctly."""
        try:
            self.analysis.export_to_excel("employee_data1.xlsx")
            obj = self.analysis.verify_excel_saved("employee_data1.xlsx")
            self.test_obj.yakshaAssert("TestExportToExcel", obj, "functional")
            print("TestExportToExcel = Passed" if obj else "TestExportToExcel = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestExportToExcel", False, "functional")
            print("TestExportToExcel = Failed")
