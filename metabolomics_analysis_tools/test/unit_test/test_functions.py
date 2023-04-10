import metabolomics_analysis_tools.data_preprocessing.normalization as nm
import metabolomics_analysis_tools.data_preprocessing.transformation as tf
import metabolomics_analysis_tools.data_preprocessing.data_reading as dp
import pandas as pd  # need to be installed
import numpy as np  # need to be installed
import pytest


# test functions for each module
# file processsing
input_data = dp.read_data_file()


def test_read_file():
    assert input_data.shape == (
        77,
        65,
    ), f'{"function passed the test, file read successfully"}'


def test_empty_input():
    # Test with empty input
    input_data = ""
    expected_output = "Error: empty input"
    assert (
        dp.read_data_file(file_path=input_data) == expected_output
    ), f'{"function passed the test, empty input"}'


# normalization
after_norm = nm.normalize_by_sum(input_data).iloc[:, 2:].sum(axis=0)


def test_normalization_sum():
    assert after_norm[0:].sum(axis=0) == len(
        after_norm
    ), f'{"function passed the test, normalization by sum is working"}'


# transformation
def test_data_transformation_log():
    # Create a sample input DataFrame
    input_data = pd.DataFrame(
        {"A": [1, 2, 3], "B": [4, 5, 6], "C": [10, 100, 1000], "D": [20, 200, 2000]}
    )
    # Call the data_transformation_log function with the input_data
    transformed_data = tf.data_transformation_log(input_data)
    # Manually calculate the expected transformed data
    expected_data = input_data.copy()
    expected_data.iloc[:, 2:] = np.log10(input_data.iloc[:, 2:])
    # Check if the transformed_data is equal to the expected_data
    pd.testing.assert_frame_equal(
        transformed_data, expected_data
    ), f'{"function passed the test"}'


def test_data_transformation_log_non_positive_values():
    # Create a sample input DataFrame with a non-positive value
    input_data = pd.DataFrame(
        {
            "A": [1, 2, 3],
            "B": [4, 5, 6],
            "C": [10, 0, 1000],  # Zero value in column C
            "D": [20, 200, 2000],
        }
    )

    # Test if the function raises a ValueError for non-positive values
    with pytest.raises(ValueError) as excinfo:
        tf.data_transformation_log(input_data)

    assert str(excinfo.value) == "Error: Non-positive values found in input data"
