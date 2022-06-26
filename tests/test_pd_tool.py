from unittest import TestCase

import pandas as pd
from pandas.testing import assert_frame_equal

from tool.pd_tool import PandasTool

# $ python -m unittest discover tests
class TestPandasTool(TestCase):
    def test_return_df_specified_columns(self):
        test_data = {
            "test_column1": ["1", "2", "3"],
            "test_column2": ["data1", "data2", "data3"],
            "test_column3": [101, 102, 103]
        }
        expected_data = {
            "test_column1": ["1", "2", "3"],
            "test_column3": [101, 102, 103]
        }
        expected_df = pd.DataFrame(expected_data)
        
        test_df = pd.DataFrame(test_data)
        test_columns_list = ["test_column1", "test_column3"]
        actural_df = PandasTool().return_df_specified_columns(test_df, test_columns_list)

        assert_frame_equal(expected_df, actural_df)