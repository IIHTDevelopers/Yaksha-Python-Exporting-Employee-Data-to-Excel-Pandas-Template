import unittest
import numpy as np
from mainclass import EmployeeDataAnalysis
from test.TestUtils import TestUtils
import pandas as pd
from io import BytesIO

class TestExportExcel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.analysis = EmployeeDataAnalysis("employee_data.csv")
        cls.test_obj = TestUtils()

    def test_empty_dataframe_export(self):
        """Test exporting an empty DataFrame to Excel."""
        try:
            with BytesIO() as buffer:
                self.analysis.export_to_excel(buffer)
                buffer.seek(0)  # Seek back to the beginning to simulate reading the file
                file_content = buffer.read()
                obj = len(file_content) > 0
                self.test_obj.yakshaAssert("TestEmptyDataFrameExport", obj, "boundary")
                print("TestEmptyDataFrameExport = Passed" if obj else "TestEmptyDataFrameExport = Failed")
        except Exception as e:
            print(f"TestEmptyDataFrameExport = Failed due to {e}")
            self.test_obj.yakshaAssert("TestEmptyDataFrameExport", False, "boundary")
            print("TestEmptyDataFrameExport = Failed")