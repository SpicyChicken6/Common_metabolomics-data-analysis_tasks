import numpy as np
import scipy.stats as stats
from numpy.random import randn

"""
these functions should be used to determine if log transformations are needed for the data
"""


def normal_dist_check(input_data):
    """
    Checks for normality in the data by performing a shapiro test.

    Args:
        input_data (pandas.DataFrame): Dataframe containing the data

    Returns:
        true if the data is normal based on shapiro test, false otherwise.
    """

    data_to_check = input_data.iloc[:, 2:]
    result = stats.shapiro(data_to_check)

    return result[1] < 0.05


def levenes_check(input_data):
    """
    Checks for homoscedasticity by performing a levene test.

    Args:
        input_data (pandas.DataFrame): Dataframe containing the data

    Returns:
        true if the data is homoscedastic based on levene test, false otherwise.
    """

    data_to_check = input_data.iloc[:, 2:]
    result = stats.levene(data_to_check)

    return result[1] < 0.05
