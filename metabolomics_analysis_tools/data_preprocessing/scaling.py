def data_scaling_mean_centered(normalized_data):
    """
    Scale the data by subtracting the mean of each column from each value in the column

    Args:
        input_data (pandas.DataFrame): Dataframe containing the data

    Returns:
        pandas.DataFrame: Scaled dataframe
    """

    data_scaled = normalized_data.iloc[:, 2:].subtract(
        normalized_data.mean(axis=0), axis=1
    )
    scaled_data = normalized_data.copy()
    scaled_data.iloc[:, 2:] = data_scaled

    return scaled_data
