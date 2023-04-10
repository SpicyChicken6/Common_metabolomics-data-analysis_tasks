import numpy as np
def data_transformation_log(input_data):
    """
    Transform the data by taking the log10 of each value

    Args:
        input_data (pandas.DataFrame): Dataframe containing the data

    Returns:
        pandas.DataFrame: Transformed dataframe
    """

    data_to_process = input_data.iloc[:, 2:]

    if (data_to_process <= 0).any().any():
        raise ValueError("Error: Non-positive values found in input data")
    data_log10 = data_to_process.apply(np.log10)
    transformed_data = input_data.copy()
    transformed_data.iloc[:, 2:] = data_log10

    return transformed_data
